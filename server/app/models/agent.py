from pydantic import BaseModel, Field
from typing import Optional


class Agent(BaseModel):
    id: str = Field(..., description="Agent unique identifier")
    name: str
    skills: list[str] = []
    online: bool = False
    current_conversations: int = 0
    max_conversations: int = 3
    status: Optional[str] = None  # available, busy, away, offline