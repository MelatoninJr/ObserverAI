# examples/simple_swarm_test.py
import os
import sys
import asyncio
from dotenv import load_dotenv

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from swarms import Agent
from swarm_models import OpenAIChat
from observer.core import Observer
from observer.adapters import wrap_swarm_agent

async def test_single_agent():
    print("\nTesting Single Agent...")
    
    # Initialize OpenAI model
    model = OpenAIChat(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model_name="gpt-4",
        temperature=0.1
    )
    
    # Create a single agent
    agent = Agent(
        agent_name="Analyzer",
        system_prompt="You are an analyst. Provide clear, structured analysis with explicit reasoning.",
        llm=model,
        max_loops=1
    )
    
    # Wrap agent with observer
    observed_agent = wrap_swarm_agent(agent)
    
    # Run agent
    task = "Analyze the current state of AI and provide three key trends"
    result = await observed_agent.run(task)
    
    return result

async def main():
    # Load environment variables
    load_dotenv()
    
    # Create observer
    observer = Observer()
    
    print("Starting SWARM test...\n")
    
    with observer.session("swarm_test") as session_id:
        try:
            # Test single agent
            result = await test_single_agent()
            print("\nAgent Result:")
            print(result)
            
            # Get metrics
            metrics = observer.get_session_metrics(session_id)
            print("\nSession Metrics:")
            print(f"Duration: {metrics['duration']:.2f} seconds")
            print(f"Total decisions tracked: {metrics['decision_count']}")
            print(f"Agents involved: {metrics['agents']}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            import traceback
            print(traceback.format_exc())

if __name__ == "__main__":
    asyncio.run(main())