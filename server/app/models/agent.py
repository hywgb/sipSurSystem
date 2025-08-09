from pydantic import BaseModel, Field, field_validator
from typing import Optional


class Agent(BaseModel):
    id: str = Field(..., description="Agent unique identifier")
    name: str
    skills: list[str] = []
    online: bool = False
    current_conversations: int = 0
    max_conversations: int = 3
    status: Optional[str] = None  # available, busy, away, offline

    @field_validator("max_conversations")
    @classmethod
    def positive_max(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("max_conversations must be > 0")
        return v

    @property
    def available(self) -> bool:
        return self.online and (self.current_conversations < self.max_conversations)