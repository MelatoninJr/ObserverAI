from typing import List, Dict, Any
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..schemas.models import Decision

class DecisionAnalyzer:
    """Basic analyzer for agent decisions."""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_success_rate(self, agent_id: Optional[str] = None) -> Dict[str, float]:
        """Calculate success rate for all agents or a specific agent."""
        stmt = select(Decision)
        if agent_id:
            stmt = stmt.where(Decision.agent_id == agent_id)
        
        result = await self.session.execute(stmt)
        decisions = result.scalars().all()
        
        success_rates = {}
        for decision in decisions:
            agent = decision.agent_id
            if agent not in success_rates:
                success_rates[agent] = {'success': 0, 'total': 0}
            
            success_rates[agent]['total'] += 1
            if decision.outcome == 'success':
                success_rates[agent]['success'] += 1
        
        return {
            agent: stats['success'] / stats['total']
            for agent, stats in success_rates.items()
            if stats['total'] > 0
        }

    async def get_common_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Identify common decision patterns and their outcomes."""
        stmt = select(Decision)
        result = await self.session.execute(stmt)
        decisions = result.scalars().all()
        
        patterns = {}
        for decision in decisions:
            pattern = f"{decision.context} -> {decision.chosen_option}"
            if pattern not in patterns:
                patterns[pattern] = {'success': 0, 'failure': 0, 'total': 0}
            
            patterns[pattern]['total'] += 1
            if decision.outcome == 'success':
                patterns[pattern]['success'] += 1
            else:
                patterns[pattern]['failure'] += 1
        
        return {
            pattern: {
                'success_rate': stats['success'] / stats['total'],
                'total_uses': stats['total']
            }
            for pattern, stats in patterns.items()
            if stats['total'] > 0
        }