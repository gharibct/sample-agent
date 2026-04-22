import os
from enum import Enum
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import AzureChatOpenAI

load_dotenv()


class LLMProvider(str, Enum):
    CLAUDE = "claude"
    AZURE_OPENAI = "azure_openai"


def get_llm(provider: LLMProvider = None):
    if provider is None:
        provider = LLMProvider(os.getenv("LLM_PROVIDER", "azure_openai").lower())

    if provider == LLMProvider.CLAUDE:
        return ChatAnthropic(
            model="claude-sonnet-4-6",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
        )
    elif provider == LLMProvider.AZURE_OPENAI:
        azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME") or os.getenv("AZURE_OPENAI_DEPLOYMENT")
        if not azure_deployment:
            raise ValueError(
                "Azure OpenAI deployment name is not configured. "
                "Set AZURE_OPENAI_DEPLOYMENT_NAME or AZURE_OPENAI_DEPLOYMENT."
            )

        return AzureChatOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=azure_deployment,
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
