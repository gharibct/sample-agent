from typing import Literal
from pydantic import BaseModel
from langchain_core.messages import SystemMessage, HumanMessage
from config import get_llm

SUPERVISOR_SYSTEM_PROMPT = """You are the ERP Assistant Supervisor. Your job is to understand the user's intent and route them to the correct manager.

Available managers:
- finance_master: Handles creation and maintenance of Finance master data — Accounts, Cost Centers, Finance Years
- scm_master: Handles creation and maintenance of SCM master data — Suppliers, Warehouses

Rules:
- If the request is clearly finance-related, route to finance_master.
- If the request is clearly SCM-related, route to scm_master.
- If the request is ambiguous or unrelated to ERP masters, respond with FINISH and politely inform the user.
- If the conversation is complete (user says thanks, bye, done, etc.), respond with FINISH.

Respond only with the route decision — do not answer the user's question yourself.
"""


class RouteDecision(BaseModel):
    next: Literal["finance_master", "scm_master", "FINISH"]
    reason: str


def get_route(state, llm=None) -> RouteDecision:
    if llm is None:
        llm = get_llm()

    structured_llm = llm.with_structured_output(RouteDecision)

    messages = [SystemMessage(content=SUPERVISOR_SYSTEM_PROMPT)] + state["messages"]
    return structured_llm.invoke(messages)
