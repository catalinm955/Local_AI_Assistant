from local_ai_assistant.config.llm import LLM_CONFIG
from local_ai_assistant.llm.clients.ollama import OllamaClient


def get_llm_client():
    provider = LLM_CONFIG["provider"]

    if provider == "ollama":
        client = OllamaClient(
            model=LLM_CONFIG["model"],
            url=LLM_CONFIG["url"]
        )
    else:
        raise ValueError(f"The selected provider '{provider}' is not implemented!")

    return client