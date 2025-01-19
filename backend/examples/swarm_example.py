import os
import sys
import asyncio
from pprint import pprint

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from observer.core import Observer, DecisionPath
from observer.adapters.enhanced_agent import EnhancedAgent

async def main():
    observer = Observer()
    agent = EnhancedAgent("investment_analyst")
    
    print("Starting detailed analysis...\n")
    
    with observer.session("investment_analysis") as session_id:
        try:
            # Execute the analysis
            decision_path = await agent.analyze_investment_opportunity()
            
            # Track the complete decision process
            observer.track_decision(
                agent_id=agent.name,
                inputs={"task": decision_path.task},
                outputs=decision_path.model_dump(),
                metadata={
                    "confidence": decision_path.outcome.get("confidence"),
                    "steps_taken": len(decision_path.steps),
                    "metrics": decision_path.metrics
                }
            )
            
            # Print detailed analysis
            print("Decision Analysis Report")
            print("=======================")
            print(f"\nTask: {decision_path.task}")
            
            print("\nSteps Taken:")
            for step in decision_path.steps:
                print(f"\n- {step['name']}")
                print(f"  Outputs: {step['outputs']}")
                if step['reasoning']:
                    print(f"  Reasoning: {step['reasoning']}")
            
            print("\nFinal Decision:")
            print(f"Choice: {decision_path.outcome['decision']}")
            print(f"Confidence: {decision_path.outcome['confidence']:.2f}")
            print("\nReasoning:")
            for key, value in decision_path.outcome['reasoning'].items():
                print(f"- {key}: {value}")
            
            # Get and print metrics
            if decision_path.metrics:
                print("\nMetrics:")
                for key, value in decision_path.metrics.items():
                    print(f"- {key}: {value}")
            
            # Get and print observer metrics
            metrics = observer.get_session_metrics(session_id)
            print("\nSession Metrics:")
            print(f"Duration: {metrics['duration']:.2f} seconds")
            print(f"Decision count: {metrics['decision_count']}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            raise

if __name__ == "__main__":
    asyncio.run(main())