import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

from graph import erp_graph
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


def print_response(result: dict):
    messages = result.get("messages", [])
    for msg in reversed(messages):
        if isinstance(msg, AIMessage) and msg.content:
            content = msg.content
            # Handle cases where content is a list (structured output)
            if isinstance(content, list):
                text_parts = [item["text"] for item in content if isinstance(item, dict) and item.get("type") == "text"]
                content = "\n".join(text_parts)
            if content and isinstance(content, str) and content.strip():
                print(f"\nERP Assistant: {content}\n")
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
