# observer/adapters/__init__.py
from .base import BaseAgentAdapter, GenericAgentAdapter
from .swarms import SwarmAdapter, wrap_swarm_agent
from .enhanced_agent import EnhancedAgent

__all__ = [
    'BaseAgentAdapter',
    'GenericAgentAdapter',
    'SwarmAdapter',
    'wrap_swarm_agent',
    'EnhancedAgent'
]