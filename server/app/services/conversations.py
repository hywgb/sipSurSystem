from typing import Dict, List, Optional
from datetime import datetime
from ..models.conversation import Conversation, Message
from .acd import acd_service


class ConversationService:
    def __init__(self) -> None:
        self._convs: Dict[str, Conversation] = {}
        self._msgs: Dict[str, List[Message]] = {}

    def create(self, conv: Conversation) -> Conversation:
        self._convs[conv.id] = conv
        self._msgs.setdefault(conv.id, [])
        # try auto-assign
        acd_service.assign(conv)
        return conv

    def get(self, conv_id: str) -> Optional[Conversation]:
        return self._convs.get(conv_id)

    def list(self, status: Optional[str] = None) -> List[Conversation]:
        values = list(self._convs.values())
        return [c for c in values if (status is None or c.status == status)]

    def add_message(self, msg: Message) -> Message:
        if msg.conversation_id not in self._msgs:
            self._msgs[msg.conversation_id] = []
        self._msgs[msg.conversation_id].append(msg)
        return msg

    def messages(self, conv_id: str) -> List[Message]:
        return list(self._msgs.get(conv_id, []))

    def close(self, conv_id: str, reason: str | None = None) -> Optional[Conversation]:
        conv = self._convs.get(conv_id)
        if not conv:
            return None
        conv.status = "closed"
        conv.closed_at = datetime.utcnow()
        acd_service.release(conv)
        if reason:
            self.add_message(
                Message(
                    id=f"sys-{conv_id}-{int(conv.closed_at.timestamp())}",
                    conversation_id=conv_id,
                    sender="system",
                    content=f"conversation closed: {reason}",
                )
            )
        return conv


conversation_service = ConversationService()