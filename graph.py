from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from state import ERPState
from supervisor import get_route
from agents.finance_master import create_finance_agent
from agents.scm_master import create_scm_agent
from config import get_llm

# --- Node: Supervisor ---
def supervisor_node(state: ERPState):
    llm = get_llm()
    decision = get_route(state, llm)

    if decision.next == "FINISH":
        return Command(goto=END, update={"current_agent": "none"})

    return Command(goto=decision.next, update={"current_agent": decision.next})


# --- Node: Finance Master Manager ---
def finance_master_node(state: ERPState):
    llm = get_llm()
    agent = create_finance_agent(llm)
    result = agent.invoke({"messages": state["messages"]})
    return Command(
        goto="supervisor",
        update={
            "messages": result["messages"],
            "current_agent": "finance_master",
        },
    )


# --- Node: SCM Master Manager ---
def scm_master_node(state: ERPState):
    llm = get_llm()
    agent = create_scm_agent(llm)
    result = agent.invoke({"messages": state["messages"]})
    return Command(
        goto="supervisor",
        update={
            "messages": result["messages"],
            "current_agent": "scm_master",
        },
    )


def build_graph():
    graph = StateGraph(ERPState)

    graph.add_node("supervisor", supervisor_node)
    graph.add_node("finance_master", finance_master_node)
    graph.add_node("scm_master", scm_master_node)

    graph.add_edge(START, "supervisor")

    return graph.compile()


erp_graph = build_graph()
