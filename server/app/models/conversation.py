from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

Channel = Literal["voice", "chat", "email", "sms"]


class Message(BaseModel):
    id: str
    conversation_id: str
    sender: Literal["customer", "agent", "system"]
    content: str
    ts: datetime = Field(default_factory=datetime.utcnow)


class Conversation(BaseModel):
    id: str
    customer_id: str
    agent_id: Optional[str] = None
    channel: Channel
    required_skill: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    closed_at: Optional[datetime] = None
    status: Literal["new", "queued", "assigned", "closed"] = "new"
    subject: Optional[str] = None
    tags: list[str] = []


class CloseConversation(BaseModel):
    reason: Optional[str] = None