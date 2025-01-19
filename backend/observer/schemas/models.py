from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime
import uuid

class Decision(BaseModel):
    """Model representing a single decision point in an agent's execution."""
    decision_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    agent_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    context: str
    options_considered: List[str]
    chosen_option: str
    reasoning: str
    outcome: Optional[str] = None
    performance_metrics: Optional[Dict] = None
    dependencies: Optional[List[str]] = None

# observer/core/tracking.py
from typing import List, Dict, Optional, Any, ContextManager
from contextlib import contextmanager
from ..schemas.models import Decision
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert

class DecisionTracker:
    """Core class for tracking agent decisions."""
    
    def __init__(self, session: AsyncSession):
        self.session = session
        self.current_decision: Optional[Decision] = None
    
    @contextmanager
    async def track(self, agent_id: str, context: str, options: List[str]) -> ContextManager[Decision]:
        """Context manager for tracking a decision."""
        try:
            self.current_decision = Decision(
                agent_id=agent_id,
                context=context,
                options_considered=options,
                chosen_option="",
                reasoning=""
            )
            yield self.current_decision
        finally:
            if self.current_decision:
                # Save to database
                stmt = insert(Decision).values(**self.current_decision.model_dump())
                await self.session.execute(stmt)
                await self.session.commit()
    
    async def record_outcome(self, decision_id: str, outcome: str, metrics: Optional[Dict[str, Any]] = None):
        """Record the outcome of a decision."""
        stmt = (
            select(Decision)
            .where(Decision.decision_id == decision_id)
        )
        result = await self.session.execute(stmt)
        decision = result.scalar_one_or_none()
        
        if decision:
            decision.outcome = outcome
            decision.performance_metrics = metrics
            await self.session.commit()