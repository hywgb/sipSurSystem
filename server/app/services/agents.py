from typing import Dict, List
from ..models.agent import Agent


class AgentService:
    def __init__(self) -> None:
        self._agents: Dict[str, Agent] = {}

    def upsert(self, agent: Agent) -> Agent:
        self._agents[agent.id] = agent
        return agent

    def get(self, agent_id: str) -> Agent | None:
        return self._agents.get(agent_id)

    def list(self) -> List[Agent]:
        return list(self._agents.values())

    def delete(self, agent_id: str) -> None:
        self._agents.pop(agent_id, None)


agent_service = AgentService()