from local_ai_assistant.config.llm import LLMConfig
from local_ai_assistant.llm.clients.ollama import OllamaClient
from local_ai_assistant.llm.clients.openai import OpenAIClient
from local_ai_assistant.llm.base import BaseLLMClient
from local_ai_assistant import exceptions


providers: dict[str, type[BaseLLMClient]] = {
    "ollama": OllamaClient,
    "openai": OpenAIClient
}

def get_llm_client(llm_config: LLMConfig) -> BaseLLMClient:

    if llm_config.provider not in providers:
        raise exceptions.InvalidLLMProviderError(
            f"The config provider '{llm_config.provider}' is not defined. \nPlease choose from [{'; '.join(providers.keys())}]"
        )
    provider = llm_config.provider
    client_class = providers[provider]
    client = client_class(llm_config)

    return client
