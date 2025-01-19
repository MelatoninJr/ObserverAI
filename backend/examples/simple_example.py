import os
import sys
import asyncio
from datetime import datetime

# Add the observer package to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from observer.core.observer import Observer

class SimpleAgent:
    """A simple agent for testing the observer."""
    
    def __init__(self, name: str):
        self.name = name
    
    async def run(self, task: str) -> str:
        # Simulate some work
        await asyncio.sleep(1)
        return f"Completed task: {task}"

async def main():
    # Create an observer
    observer = Observer()
    
    # Create a simple agent
    agent = SimpleAgent("test_agent")
    
    # Start an observation session
    with observer.session("test_session") as session_id:
        try:
            # Track the agent's decision
            start_time = datetime.now()
            
            # Run the agent
            result = await agent.run("test task")
            
            # Record the decision
            observer.track_decision(
                agent_id=agent.name,
                inputs={"task": "test task"},
                outputs={"result": result},
                metadata={
                    "response_time": (datetime.now() - start_time).total_seconds(),
                    "success": True
                }
            )
            
            print(f"Agent result: {result}")
            
            # Get and print metrics
            metrics = observer.get_session_metrics(session_id)
            print("\nSession metrics:")
            print(f"Duration: {metrics['duration']:.2f} seconds")
            print(f"Decision count: {metrics['decision_count']}")
            print(f"Agents involved: {metrics['agents']}")
            print(f"Averages: {metrics['averages']}")
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())