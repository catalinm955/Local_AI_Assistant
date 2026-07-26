from local_ai_assistant.config.llm import LLM_CONFIG
from local_ai_assistant.llm.clients.ollama import OllamaClient
from local_ai_assistant.llm.clients.openai import OpenAIClient


def get_llm_client():
    provider = LLM_CONFIG["provider"]

    if provider == "ollama":
        client = OllamaClient(
            model=LLM_CONFIG["model"],
            url=LLM_CONFIG["url"]
        )

    elif provider == "openai":
        client = OpenAIClient(
            model=LLM_CONFIG["model"],
            url=LLM_CONFIG["url"],
            api_key=LLM_CONFIG["api_key"]
        )
    else:
        raise ValueError(f"The selected provider '{provider}' is not implemented!")

    return client