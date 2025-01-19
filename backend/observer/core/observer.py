# observer/core/observer.py
from typing import Any, Dict, List, Optional
from datetime import datetime
import uuid
from contextlib import contextmanager

class Observer:
    """Core observer class that can be attached to any agent framework."""
    
    def __init__(self):
        self.observations = {}
        self.current_session = None
    
    @contextmanager
    def session(self, session_name: Optional[str] = None):
        """Create a new observation session."""
        session_id = session_name or str(uuid.uuid4())
        self.current_session = session_id
        self.observations[session_id] = {
            'start_time': datetime.now(),
            'end_time': None,  # Will be set when session ends
            'decisions': [],
            'metrics': {
                'total_tokens': 0,
                'total_time': 0,
                'success_count': 0,
                'failure_count': 0
            }
        }
        
        try:
            yield session_id
        finally:
            if self.current_session:
                self.observations[self.current_session]['end_time'] = datetime.now()
                self.current_session = None
    
    def track_decision(self, 
                      agent_id: str,
                      inputs: Dict[str, Any],
                      outputs: Dict[str, Any],
                      metadata: Optional[Dict[str, Any]] = None):
        """Track a single decision point."""
        if not self.current_session:
            raise RuntimeError("No active session. Use 'with observer.session():' to create one.")
            
        decision = {
            'timestamp': datetime.now(),
            'agent_id': agent_id,
            'inputs': inputs,
            'outputs': outputs,
            'metadata': metadata or {}
        }
        
        self.observations[self.current_session]['decisions'].append(decision)
    
    def get_session_metrics(self, session_id: str) -> Dict[str, Any]:
        """Get metrics for a specific session."""
        if session_id not in self.observations:
            raise KeyError(f"Session {session_id} not found")
            
        session = self.observations[session_id]
        decisions = session['decisions']
        
        # Handle case where session might still be ongoing
        end_time = session['end_time'] or datetime.now()
        duration = (end_time - session['start_time']).total_seconds()
        
        metrics = {
            'duration': duration,
            'decision_count': len(decisions),
            'agents': set(d['agent_id'] for d in decisions),
            'averages': self._calculate_averages(decisions)
        }
        
        return metrics
    
    def _calculate_averages(self, decisions: List[Dict]) -> Dict[str, float]:
        """Calculate average metrics from decisions."""
        if not decisions:
            return {
                'avg_response_time': 0,
                'avg_token_usage': 0,
                'success_rate': 0
            }
            
        totals = {
            'response_time': 0,
            'token_usage': 0,
            'success_rate': 0
        }
        
        for decision in decisions:
            metadata = decision['metadata']
            totals['response_time'] += metadata.get('response_time', 0)
            totals['token_usage'] += metadata.get('token_usage', 0)
            totals['success_rate'] += 1 if metadata.get('success', False) else 0
        
        count = len(decisions)
        return {
            'avg_response_time': totals['response_time'] / count,
            'avg_token_usage': totals['token_usage'] / count,
            'success_rate': (totals['success_rate'] / count) * 100
        }