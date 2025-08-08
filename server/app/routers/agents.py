from fastapi import APIRouter, HTTPException
from ..models.agent import Agent
from ..services.agents import agent_service

router = APIRouter(prefix="/agents", tags=["agents"])


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