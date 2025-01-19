ObserverAI 🔍🤖

Follow us on Twitter for updates: [@ObserverAI](https://twitter.com/ObserverAgent)

ObserverAI is an advanced framework for tracking and analyzing AI agent decision paths. Designed to provide deep insights into AI behavior, ObserverAI equips developers and researchers with tools to understand, evaluate, and enhance the decision-making processes of AI agents.

Key Features ✨

Comprehensive Decision Tracking: Record decisions made by AI agents, capturing context, evaluated options, chosen outcomes, and underlying reasoning.

Session Management: Organize and analyze decision paths within structured observation sessions.

Versatile Agent Adapters: Seamless integration with various agent types, including Enhanced Agents and SWARM Agents.

Robust Metrics and Analytics: Generate actionable insights through success metrics, trend analyses, and decision pattern recognition.

Installation ⚙️

ObserverAI uses Poetry for dependency management. To get started, clone the repository and install the dependencies:

# Clone the repository
git clone https://github.com/your-repo/ObserverAI.git

# Navigate to the project directory
cd ObserverAI

# Install dependencies
poetry install

Configuration ⚖️

Set up the required environment variables by creating a .env file in the root directory. Example:

# Example .env file
DATABASE_URL=sqlite:///observerai.db
API_KEY=your_api_key
DEBUG=True

Usage 🔄

Example: Enhanced Agent ✨

This example demonstrates how to use the EnhancedAgent to analyze investment opportunities:

from observerai.agents import EnhancedAgent
from observerai.observer import Observer

observer = Observer()
agent = EnhancedAgent()

with observer.session("Investment Analysis") as session:
    decision = agent.analyze_investment("Opportunity X")
    session.record(decision)

Example: SWARM Agent 🔰

Use the SwarmAdapter to observe decisions made by SWARM agents:

from observerai.adapters import SwarmAdapter
from observerai.observer import Observer

observer = Observer()
swarm_adapter = SwarmAdapter()

with observer.session("AI State Analysis") as session:
    decision = swarm_adapter.analyze_state("Current AI Trends")
    session.record(decision)

Example: Simple Agent 📚

For quick tests, the SimpleAgent provides an easy way to track basic decision-making:

from observerai.agents import SimpleAgent
from observerai.observer import Observer

observer = Observer()
agent = SimpleAgent()

with observer.session("Testing") as session:
    decision = agent.make_decision("Sample Task")
    session.record(decision)

Core Components 🔄

Observer ⚡

The Observer class manages observation sessions, ensuring decisions are systematically tracked and stored for analysis.

Decision Path 🎯

The DecisionPath class encapsulates the steps, context, and reasoning behind an agent's decision.

Enhanced Agent 🧪

The EnhancedAgent class offers structured methods for tackling complex tasks, providing detailed decision pathways and analytics.

SWARM Adapter 🤗

The SwarmAdapter converts outputs from SWARM agents into a standardized format, enabling seamless observation and analysis.

Development ⚒️

Running Tests 🛠️

ObserverAI includes a comprehensive test suite. Run the tests using:

poetry run pytest

Code Formatting 🔧

Ensure consistent code style with:

poetry run black .

License 🔒

This project is licensed under the MIT License. See the LICENSE file for details.

Authors 👤

Your Name

Acknowledgments 🌟

Special thanks to the open-source community and contributors for their invaluable support and collaboration.