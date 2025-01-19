import os
import sys
import asyncio
from dotenv import load_dotenv

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from observer.core import Observer
from observer.adapters.enhanced_agent import EnhancedAgent

async def main():
    # Load environment variables
    load_dotenv()
    
    observer = Observer()
    agent = EnhancedAgent("investment_analyst")
    
    # List of companies to analyze
    companies = ["Apple", "Microsoft", "Tesla"]
    
    print("Starting investment analysis...\n")
    
    with observer.session("investment_analysis") as session_id:
        for company in companies:
            try:
                print(f"Analyzing {company}...")
                
                # Execute the analysis
                decision_path = await agent.analyze_investment_opportunity(company)
                
                # Track the decision process
                observer.track_decision(
                    agent_id=agent.name,
                    inputs={"company": company},
                    outputs=decision_path.model_dump(),
                    metadata={
                        "confidence": decision_path.confidence_score,
                        "steps_taken": len(decision_path.steps)
                    }
                )
                
                # Print analysis
                print(f"\nDecision Analysis Report for {company}")
                print("=" * 50)
                
                print("\nAnalysis Steps:")
                for step in decision_path.steps:
                    print(f"\n{step.thought}:")
                    print("-" * len(step.thought))
                    print(f"Confidence: {step.confidence.value}")
                    print("\nReasoning:")
                    print(step.reasoning)
                    
                    if step.alternatives_considered:
                        print("\nAlternatives Considered:")
                        for alt in step.alternatives_considered:
                            print(f"\nApproach: {alt.get('approach', 'N/A')}")
                            print(f"Feasibility: {alt.get('feasibility', 'N/A')}/10")
                            print(f"Advantages: {alt.get('advantages', 'N/A')}")
                            print(f"Disadvantages: {alt.get('disadvantages', 'N/A')}")
                
                print("\nFinal Decision:")
                print(f"Decision: {decision_path.final_decision}")
                print(f"Confidence: {decision_path.confidence_score:.2f}")
                
                if decision_path.reasoning_chain:
                    print("\nReasoning Chain:")
                    if "final_reasoning" in decision_path.reasoning_chain:
                        print(decision_path.reasoning_chain["final_reasoning"])
                
            except Exception as e:
                print(f"Error analyzing {company}: {e}")
                import traceback
                print(traceback.format_exc())
        
        # Get and print overall metrics
        metrics = observer.get_session_metrics(session_id)
        print("\nSession Metrics:")
        print(f"Duration: {metrics['duration']:.2f} seconds")
        print(f"Companies analyzed: {metrics['decision_count']}")

if __name__ == "__main__":
    asyncio.run(main())