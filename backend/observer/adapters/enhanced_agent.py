import asyncio
from typing import List, Dict, Any, Optional
import os
from openai import OpenAI
from enum import Enum
from pydantic import BaseModel, Field

class DecisionConfidence(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class ThoughtStep(BaseModel):
    thought: str
    reasoning: str
    confidence: DecisionConfidence
    supporting_evidence: Dict[str, Any] = Field(default_factory=dict)
    alternatives_considered: List[Dict[str, Any]] = Field(default_factory=list)

class DecisionPath(BaseModel):
    task: str
    context: Dict[str, Any] = Field(default_factory=dict)
    steps: List[ThoughtStep] = Field(default_factory=list)
    final_decision: Optional[str] = None
    confidence_score: float = 0.0
    reasoning_chain: Optional[Dict[str, Any]] = None

class EnhancedAgent:
    def __init__(self, name: str, model: str = "gpt-4"):
        self.name = name
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def analyze_task(self, task: str, context: Dict[str, Any]) -> DecisionPath:
        """
        Analyze any task using a structured decision-making process
        
        Args:
            task: The task or question to analyze
            context: Additional context or parameters for the analysis
        """
        decision = DecisionPath(
            task=task,
            context=context,
            steps=[]
        )

        # Step 1: Initial Problem Analysis
        analysis_prompt = self._create_analysis_prompt(task, context)
        initial_analysis = await self._get_llm_response(analysis_prompt)
        decision.steps.append(ThoughtStep(
            thought="Initial Problem Analysis",
            reasoning=initial_analysis,
            confidence=self._determine_confidence(initial_analysis),
            supporting_evidence={"context": context},
            alternatives_considered=[]
        ))

        # Step 2: Generate Alternatives
        alternatives_prompt = self._create_alternatives_prompt(task, initial_analysis)
        alternatives = await self._get_llm_response(alternatives_prompt)
        decision.steps.append(ThoughtStep(
            thought="Alternative Solutions",
            reasoning="Exploring different approaches",
            confidence=self._determine_confidence(alternatives),
            supporting_evidence={"initial_analysis": initial_analysis},
            alternatives_considered=self._parse_alternatives(alternatives)
        ))

        # Step 3: Evaluate Trade-offs
        tradeoff_prompt = self._create_tradeoff_prompt(task, alternatives)
        tradeoff_analysis = await self._get_llm_response(tradeoff_prompt)
        decision.steps.append(ThoughtStep(
            thought="Trade-off Analysis",
            reasoning=tradeoff_analysis,
            confidence=self._determine_confidence(tradeoff_analysis),
            supporting_evidence={"alternatives": alternatives},
            alternatives_considered=[]
        ))

        # Step 4: Final Decision Synthesis
        decision_prompt = self._create_decision_prompt(
            task, initial_analysis, alternatives, tradeoff_analysis
        )
        final_decision = await self._get_llm_response(decision_prompt)
        
        # Parse the final decision
        parsed_decision = self._parse_final_decision(final_decision)
        decision.final_decision = parsed_decision["decision"]
        decision.confidence_score = parsed_decision["confidence"]
        decision.reasoning_chain = {
            "initial_analysis": initial_analysis,
            "alternatives": alternatives,
            "tradeoffs": tradeoff_analysis,
            "final_reasoning": parsed_decision["reasoning"]
        }

        return decision

    async def analyze_investment_opportunity(self, company_name: str) -> DecisionPath:
        """Analyze a company as an investment opportunity using the enhanced framework"""
        return await self.analyze_task(
            task=f"Analyze investment opportunity for {company_name}",
            context={
                "company": company_name,
                "analysis_type": "investment",
                "required_aspects": [
                    "business_model",
                    "market_position",
                    "growth_potential",
                    "risks"
                ]
            }
        )

    def _create_analysis_prompt(self, task: str, context: Dict[str, Any]) -> str:
        if context.get("analysis_type") == "investment":
            return f"""
            Analyze {context['company']} as an investment opportunity. Consider:
            1. Business Model & Competitive Advantage
            2. Market Position & Industry Analysis
            3. Growth Potential & Expansion Opportunities
            4. Financial Health & Performance
            5. Management & Leadership
            6. Risks & Challenges
            
            Provide a comprehensive analysis covering each aspect.
            """
        
        return f"""
        Analyze the following task in detail:
        Task: {task}
        Context: {context}
        
        Consider:
        1. Key objectives and constraints
        2. Critical factors to consider
        3. Potential challenges and opportunities
        4. Relevant context and implications
        
        Provide a structured analysis that breaks down the problem.
        """

    def _create_alternatives_prompt(self, task: str, initial_analysis: str) -> str:
        return f"""
        Based on this analysis: {initial_analysis}
        
        Generate multiple alternative approaches for: {task}
        
        For each alternative:
        1. Describe the approach
        2. List key advantages
        3. List potential disadvantages
        4. Rate feasibility (1-10)
        
        Format each alternative as:
        START_ALTERNATIVE
        Approach: [Description]
        Advantages: [List]
        Disadvantages: [List]
        Feasibility: [1-10]
        END_ALTERNATIVE
        """

    def _create_tradeoff_prompt(self, task: str, alternatives: str) -> str:
        return f"""
        Given these alternatives: {alternatives}
        
        Analyze the trade-offs for: {task}
        
        Consider:
        1. Cost-benefit analysis
        2. Risk-reward assessment
        3. Short-term vs long-term implications
        4. Resource requirements
        
        Provide a structured comparison of the trade-offs.
        """

    def _create_decision_prompt(self, task: str, analysis: str, 
                              alternatives: str, tradeoffs: str) -> str:
        return f"""
        Based on:
        Initial Analysis: {analysis}
        Alternatives: {alternatives}
        Trade-offs: {tradeoffs}
        
        Make a final decision for: {task}
        
        Provide:
        1. Clear decision/recommendation
        2. Confidence level (0-1)
        3. Detailed reasoning
        
        Format:
        START_DECISION
        Decision: [Your decision]
        Confidence: [0-1]
        Reasoning: [Detailed explanation]
        END_DECISION
        """

    async def _get_llm_response(self, prompt: str) -> str:
        """Get response from the language model"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a rational decision-making agent. Provide detailed, structured analysis."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error getting LLM response: {e}")
            return f"Error: {str(e)}"

    def _determine_confidence(self, text: str) -> DecisionConfidence:
        """Analyze the response to determine confidence level"""
        # This is a simple implementation - could be made more sophisticated
        if "uncertain" in text.lower() or "unclear" in text.lower():
            return DecisionConfidence.LOW
        elif "likely" in text.lower() or "probably" in text.lower():
            return DecisionConfidence.MEDIUM
        else:
            return DecisionConfidence.HIGH

    def _parse_alternatives(self, alternatives_text: str) -> List[Dict[str, Any]]:
        """Parse the alternatives response into structured format"""
        alternatives = []
        current_alt = {}
        
        for line in alternatives_text.split('\n'):
            if line.startswith('START_ALTERNATIVE'):
                current_alt = {}
            elif line.startswith('Approach:'):
                current_alt['approach'] = line.split(':', 1)[1].strip()
            elif line.startswith('Advantages:'):
                current_alt['advantages'] = line.split(':', 1)[1].strip()
            elif line.startswith('Disadvantages:'):
                current_alt['disadvantages'] = line.split(':', 1)[1].strip()
            elif line.startswith('Feasibility:'):
                feasibility_text = line.split(':', 1)[1].strip()
                try:
                    # Handle cases like "8/10" or "8 out of 10"
                    if '/' in feasibility_text:
                        numerator = feasibility_text.split('/')[0].strip()
                        current_alt['feasibility'] = int(numerator)
                    elif 'out of' in feasibility_text:
                        numerator = feasibility_text.split('out of')[0].strip()
                        current_alt['feasibility'] = int(numerator)
                    else:
                        current_alt['feasibility'] = int(feasibility_text)
                except (ValueError, IndexError):
                    # Default to middle value if parsing fails
                    current_alt['feasibility'] = 5
            elif line.startswith('END_ALTERNATIVE'):
                alternatives.append(current_alt)
        
        return alternatives

    def _parse_final_decision(self, decision_text: str) -> Dict[str, Any]:
        """Parse the final decision response into structured format"""
        decision_data = {
            "decision": "",
            "confidence": 0.0,
            "reasoning": ""
        }
        
        for line in decision_text.split('\n'):
            if line.startswith('Decision:'):
                decision_data["decision"] = line.split(':', 1)[1].strip()
            elif line.startswith('Confidence:'):
                try:
                    decision_data["confidence"] = float(line.split(':', 1)[1].strip())
                except ValueError:
                    decision_data["confidence"] = 0.0
            elif line.startswith('Reasoning:'):
                decision_data["reasoning"] = line.split(':', 1)[1].strip()
        
        return decision_data