from fastapi import APIRouter, HTTPException
from ..models.conversation import Conversation, Message
from ..services.conversations import conversation_service

router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.post("")
def create_conversation(conv: Conversation) -> Conversation:
    return conversation_service.create(conv)


@router.get("")
def list_conversations(status: str | None = None) -> list[Conversation]:
    return conversation_service.list(status)


@router.get("/{conv_id}")
def get_conversation(conv_id: str) -> Conversation:
    c = conversation_service.get(conv_id)
    if not c:
        raise HTTPException(status_code=404, detail="conversation not found")
    return c


@router.post("/{conv_id}/messages")
def send_message(conv_id: str, msg: Message) -> Message:
    if msg.conversation_id != conv_id:
        raise HTTPException(status_code=400, detail="conversation_id mismatch")
    if not conversation_service.get(conv_id):
        raise HTTPException(status_code=404, detail="conversation not found")
    return conversation_service.add_message(msg)


@router.get("/{conv_id}/messages")
def list_messages(conv_id: str) -> list[Message]:
    return conversation_service.messages(conv_id)