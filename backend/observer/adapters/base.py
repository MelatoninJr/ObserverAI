# observer/adapters/base.py
from typing import Any, Dict, Optional
from ..core.decision import DecisionPath, ThoughtStep

class BaseAgentAdapter:
    """Base adapter that any agent framework can inherit from"""
    
    def convert_to_decision_path(
        self,
        task: str,
        agent_output: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> DecisionPath:
        """Convert any agent's output into our standardized decision path format"""
        decision = DecisionPath(
            task=task,
            context=context or {}
        )
        
        # Override this method to convert your agent's specific output format
        # into our standardized DecisionPath format
        return decision

    def extract_thought_steps(self, agent_output: Any) -> List[ThoughtStep]:
        """Extract thought steps from agent output"""
        # Override this to parse your agent's specific format
        return []

    def extract_final_decision(self, agent_output: Any) -> Dict[str, Any]:
        """Extract final decision from agent output"""
        # Override this to parse your agent's specific format
        return {
            "decision": "",
            "confidence": 0.0,
            "reasoning": ""
        }

class GenericAgentAdapter(BaseAgentAdapter):
    """Adapter for generic agents that don't need special handling"""
    
    def convert_to_decision_path(
        self,
        task: str,
        agent_output: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> DecisionPath:
        """Convert any structured output into a decision path"""
        decision = DecisionPath(
            task=task,
            context=context or {}
        )

        # Handle different types of agent outputs
        if isinstance(agent_output, dict):
            # Handle dictionary output
            if "steps" in agent_output:
                for step in agent_output["steps"]:
                    decision.steps.append(
                        ThoughtStep(
                            thought=step.get("thought", "Unknown thought"),
                            reasoning=step.get("reasoning", "No reasoning provided"),
                            confidence=self._determine_confidence(step),
                            supporting_evidence=step.get("evidence", {}),
                            alternatives_considered=step.get("alternatives", [])
                        )
                    )
            
            if "decision" in agent_output:
                decision.final_decision = agent_output["decision"]
                decision.confidence_score = agent_output.get("confidence", 0.0)
                decision.reasoning_chain = agent_output.get("reasoning", {})

        elif isinstance(agent_output, str):
            # Handle string output
            decision.steps.append(
                ThoughtStep(
                    thought="Direct Response",
                    reasoning=agent_output,
                    confidence="MEDIUM",
                    supporting_evidence={},
                    alternatives_considered=[]
                )
            )
            decision.final_decision = agent_output
            decision.confidence_score = 0.5

        return decision

    def _determine_confidence(self, step: Dict[str, Any]) -> str:
        confidence = step.get("confidence", "").upper()
        if confidence in ["LOW", "MEDIUM", "HIGH"]:
            return confidence
        return "MEDIUM"