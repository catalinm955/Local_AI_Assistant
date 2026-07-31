import pytest

from local_ai_assistant.llm.factory import get_llm_client
from local_ai_assistant.config.llm import LLMConfig
from local_ai_assistant.llm.clients.ollama import OllamaClient
from local_ai_assistant.llm.clients.openai import OpenAIClient
from local_ai_assistant.llm.base import BaseLLMClient
from local_ai_assistant.exceptions import InvalidLLMProviderError


@pytest.mark.parametrize(
        "provider, expected_class",
    [
        ("ollama", OllamaClient),
        ("openai", OpenAIClient)
    ]
)
def test_factory_returns_correct_client(provider: str, expected_class: type[BaseLLMClient]):
    llm_config = LLMConfig(
        provider=provider,
        model="test-model",
        base_url="test-url"
    )

    client = get_llm_client(llm_config)

    assert isinstance(client, expected_class)


def test_factory_rejects_invalid_provider():
    invalid_llm_config = LLMConfig(
        provider="invalid_provider",
        model="test-model",
        base_url="test-url"
    )

    with pytest.raises(InvalidLLMProviderError):
        get_llm_client(invalid_llm_config)
