from local_ai_assistant.config.llm import LLMConfig
from local_ai_assistant.llm.clients.ollama import OllamaClient
from local_ai_assistant.llm.clients.openai import OpenAIClient
from local_ai_assistant.llm.base import BaseLLMClient


providers: dict[str, type[BaseLLMClient]] = {
    "ollama": OllamaClient,
    "openai": OpenAIClient
}

def get_llm_client(llm_config: LLMConfig) -> BaseLLMClient:

    provider = llm_config.provider
    client_class = providers[provider]
    client = client_class(llm_config)

    return client