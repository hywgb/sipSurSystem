from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..models.agent import Agent
from ..services.agents import agent_service

router = APIRouter(prefix="/agents", tags=["agents"])


class AgentPatch(BaseModel):
    name: str | None = None
    skills: list[str] | None = None
    online: bool | None = None
    max_conversations: int | None = None
    status: str | None = None


@router.get("")
def list_agents() -> list[Agent]:
    return agent_service.list()


@router.put("/{agent_id}")
def upsert_agent(agent_id: str, agent: Agent) -> Agent:
    if agent_id != agent.id:
        raise HTTPException(status_code=400, detail="agent_id mismatch")
    return agent_service.upsert(agent)


@router.get("/{agent_id}")
def get_agent(agent_id: str) -> Agent:
    a = agent_service.get(agent_id)
    if not a:
        raise HTTPException(status_code=404, detail="agent not found")
    return a


@router.delete("/{agent_id}")
def delete_agent(agent_id: str) -> dict:
    agent_service.delete(agent_id)
    return {"deleted": True}


@router.patch("/{agent_id}")
def patch_agent(agent_id: str, patch: AgentPatch) -> Agent:
    a = agent_service.get(agent_id)
    if not a:
        raise HTTPException(status_code=404, detail="agent not found")
    data = a.model_dump()
    for k, v in patch.model_dump(exclude_none=True).items():
        data[k] = v
    updated = Agent(**data)
    return agent_service.upsert(updated)


@router.post("/{agent_id}/online")
def set_online(agent_id: str) -> Agent:
    a = agent_service.get(agent_id)
    if not a:
        raise HTTPException(status_code=404, detail="agent not found")
    a.online = True
    a.status = "available"
    return agent_service.upsert(a)


@router.post("/{agent_id}/offline")
def set_offline(agent_id: str) -> Agent:
    a = agent_service.get(agent_id)
    if not a:
        raise HTTPException(status_code=404, detail="agent not found")
    a.online = False
    a.status = "offline"
    a.current_conversations = 0
    return agent_service.upsert(a)