from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage
from config import get_llm
from tools.scm_tools import SCM_TOOLS

SCM_SYSTEM_PROMPT = """You are the SCM Master Manager for an ERP system.

Your responsibilities:
- Create and maintain Suppliers
- Create and maintain Warehouses

Guidelines:
- Always ask for ALL required fields before creating a record.
- If the user provides partial information, ask follow-up questions for the missing fields.
- Confirm with the user before executing a create or update operation.
- Be concise and professional in your responses.

Required fields:
- Supplier: supplier_code, supplier_name (contact_person, currency, country are optional)
- Warehouse: warehouse_code, warehouse_name (location, capacity are optional)
"""


def create_scm_agent(llm=None):
    if llm is None:
        llm = get_llm()
    return create_react_agent(
        model=llm,
        tools=SCM_TOOLS,
        prompt=SystemMessage(content=SCM_SYSTEM_PROMPT),
    )
