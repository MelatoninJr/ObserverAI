# observer/core/decision.py
from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, Field

class DecisionPath(BaseModel):
    """A flexible structure for capturing any agent's decision path"""
    
    task: str
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    
    # Core decision components
    context: Dict[str, Any] = {}
    steps: List[Dict[str, Any]] = []
    outcome: Dict[str, Any] = {}
    
    # Optional components
    reasoning: Optional[List[Dict[str, Any]]] = None
    metrics: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

    def add_step(self, 
                 name: str, 
                 inputs: Dict[str, Any],
                 outputs: Dict[str, Any],
                 reasoning: Optional[Dict[str, Any]] = None):
        """Add a decision step"""
        step = {
            "name": name,
            "timestamp": datetime.now(),
            "inputs": inputs,
            "outputs": outputs,
            "reasoning": reasoning
        }
        self.steps.append(step)

    def set_outcome(self, 
                   decision: Any,
                   confidence: Optional[float] = None,
                   reasoning: Optional[Dict[str, Any]] = None):
        """Set the final outcome"""
        self.outcome = {
            "decision": decision,
            "timestamp": datetime.now(),
            "confidence": confidence,
            "reasoning": reasoning
        }

    def add_metric(self, name: str, value: Any):
        """Add a performance metric"""
        if self.metrics is None:
            self.metrics = {}
        self.metrics[name] = value