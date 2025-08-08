from typing import Dict, List, Optional
from ..models.conversation import Conversation, Message


class ConversationService:
    def __init__(self) -> None:
        self._convs: Dict[str, Conversation] = {}
        self._msgs: Dict[str, List[Message]] = {}

    def create(self, conv: Conversation) -> Conversation:
        self._convs[conv.id] = conv
        self._msgs.setdefault(conv.id, [])
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


conversation_service = ConversationService()