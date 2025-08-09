from typing import Optional
from ..models.conversation import Conversation
from ..models.agent import Agent
from .agents import agent_service


class ACDService:
    def select_agent(self, conv: Conversation) -> Optional[Agent]:
        candidates = []
        for a in agent_service.list():
            if not a.online:
                continue
            if a.current_conversations >= a.max_conversations:
                continue
            if conv.required_skill and conv.required_skill not in a.skills:
                continue
            candidates.append(a)
        if not candidates:
            return None
        candidates.sort(key=lambda x: x.current_conversations)
        return candidates[0]

    def assign(self, conv: Conversation) -> Optional[Agent]:
        agent = self.select_agent(conv)
        if agent:
            conv.agent_id = agent.id
            conv.status = "assigned"
            agent.current_conversations += 1
            agent_service.upsert(agent)
        else:
            conv.status = "queued"
        return agent

    def release(self, conv: Conversation) -> None:
        if conv.agent_id:
            a = agent_service.get(conv.agent_id)
            if a and a.current_conversations > 0:
                a.current_conversations -= 1
                agent_service.upsert(a)


acd_service = ACDService()