from typing import Any, Dict, Optional
from datetime import datetime
import functools
from ..core.observer import Observer

class SwarmObserver:
    """Adapter for observing SWARM agents and workflows."""
    
    def __init__(self):
        self.observer = Observer()
    
    def observe_workflow(self, workflow: Any):
        """Wrap a SWARM workflow with observation capabilities."""
        original_run = workflow.run
        
        @functools.wraps(original_run)
        async def wrapped_run(task: str, *args, **kwargs):
            with self.observer.session(f"workflow_{id(workflow)}") as session_id:
                try:
                    # Track each agent in the workflow
                    for agent in workflow.agents:
                        # Wrap agent's execution
                        if hasattr(agent, 'run'):
                            original_agent_run = agent.run
                            start_time = datetime.now()
                            
                            try:
                                result = await original_agent_run(task, *args, **kwargs)
                                
                                # Track successful decision
                                self.observer.track_decision(
                                    agent_id=agent.agent_name,
                                    inputs={'task': task},
                                    outputs={'result': result},
                                    metadata={
                                        'response_time': (datetime.now() - start_time).total_seconds(),
                                        'success': True
                                    }
                                )
                                
                            except Exception as e:
                                # Track failed decision
                                self.observer.track_decision(
                                    agent_id=agent.agent_name,
                                    inputs={'task': task},
                                    outputs={'error': str(e)},
                                    metadata={
                                        'response_time': (datetime.now() - start_time).total_seconds(),
                                        'success': False
                                    }
                                )
                                raise
                    
                    # Execute original workflow
                    result = await original_run(task, *args, **kwargs)
                    return result
                    
                except Exception as e:
                    # Track workflow failure
                    self.observer.track_decision(
                        agent_id='workflow',
                        inputs={'task': task},
                        outputs={'error': str(e)},
                        metadata={'success': False}
                    )
                    raise
        
        workflow.run = wrapped_run
        return workflow
    
    def get_metrics(self, session_id: str) -> Dict[str, Any]:
        """Get metrics for a specific workflow session."""
        return self.observer.get_session_metrics(session_id)