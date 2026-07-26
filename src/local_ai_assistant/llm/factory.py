from local_ai_assistant.config.llm import LLM_CONFIG
from local_ai_assistant.llm.clients.ollama import OllamaClient
from local_ai_assistant.llm.clients.openai import OpenAIClient
from local_ai_assistant.llm.base import BaseLLMClient


providers: dict[str, type[BaseLLMClient]] = {
    "ollama": OllamaClient,
    "openai": OpenAIClient
}

def get_llm_client():
    
    provider = LLM_CONFIG["provider"]
    client_class = providers[provider]
    client = client_class(LLM_CONFIG)

    return client

get_llm_client()