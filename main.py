from graph import erp_graph
from langchain_core.messages import HumanMessage, AIMessage


def print_response(result: dict):
    messages = result.get("messages", [])
    for msg in reversed(messages):
        if isinstance(msg, AIMessage) and msg.content:
            print(f"\nERP Assistant: {msg.content}\n")
            break


def run():
    print("=" * 50)
    print("  ERP Assistant (Multi-Agent)")
    print("  Managers: Finance Master | SCM Master")
    print("  Type 'exit' to quit.")
    print("=" * 50)

    conversation_messages = []

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "bye"):
            print("\nERP Assistant: Goodbye!\n")
            break

        conversation_messages.append(HumanMessage(content=user_input))

        result = erp_graph.invoke({"messages": conversation_messages, "current_agent": ""})

        # Update conversation history with latest messages
        conversation_messages = result["messages"]

        print_response(result)


if __name__ == "__main__":
    run()
