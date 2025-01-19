# observer/adapters/swarm_adapter.py
from typing import Any, Dict, Optional, List
from .base import BaseAgentAdapter
from ..core.decision import DecisionPath, ThoughtStep, DecisionConfidence

class SwarmAdapter(BaseAgentAdapter):
    """Adapter specifically for SWARM agents"""
    
    def convert_to_decision_path(
        self,
        task: str,
        swarm_output: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> DecisionPath:
        """Convert SWARM output to our decision path format"""
        decision = DecisionPath(
            task=task,
            context=context or {}
        )

        # Extract thought steps from SWARM's execution path
        if hasattr(swarm_output, 'execution_path'):
            for step in swarm_output.execution_path:
                decision.steps.append(
                    ThoughtStep(
                        thought=step.get("action", "Unknown action"),
                        reasoning=step.get("reasoning", "No reasoning provided"),
                        confidence=self._convert_swarm_confidence(step.get("confidence", 0.5)),
                        supporting_evidence={"swarm_data": step.get("data", {})},
                        alternatives_considered=self._extract_swarm_alternatives(step)
                    )
                )

        # Extract final results
        if hasattr(swarm_output, 'result'):
            decision.final_decision = str(swarm_output.result)
            decision.confidence_score = getattr(swarm_output, 'confidence', 0.5)
            decision.reasoning_chain = {
                "swarm_reasoning": getattr(swarm_output, 'reasoning', {}),
                "swarm_metrics": getattr(swarm_output, 'metrics', {})
            }

        return decision

    def _convert_swarm_confidence(self, confidence: float) -> DecisionConfidence:
        """Convert SWARM confidence score to our format"""
        if confidence < 0.4:
            return DecisionConfidence.LOW
        elif confidence < 0.7:
            return DecisionConfidence.MEDIUM
        return DecisionConfidence.HIGH

    def _extract_swarm_alternatives(self, step: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract alternatives considered from SWARM step"""
        alternatives = []
        
        if "considered_actions" in step:
            for action in step["considered_actions"]:
                alternatives.append({
                    "approach": action.get("name", "Unknown"),
                    "advantages": action.get("pros", []),
                    "disadvantages": action.get("cons", []),
                    "feasibility": action.get("feasibility_score", 5)
                })
                
        return alternatives

def wrap_swarm_agent(agent: Any) -> Any:
    """Wrapper function to add observation to a SWARM agent"""
    original_execute = agent.execute
    adapter = SwarmAdapter()
    
    async def wrapped_execute(task: str, *args, **kwargs):
        # Execute original SWARM agent
        result = await original_execute(task, *args, **kwargs)
        
        # Convert result to our format
        decision_path = adapter.convert_to_decision_path(
            task=task,
            swarm_output=result,
            context=kwargs.get('context', {})
        )
        
        return {
            "original_result": result,
            "decision_path": decision_path
        }
    
    agent.execute = wrapped_execute
    return agent