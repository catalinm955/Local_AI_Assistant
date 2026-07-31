import pytest
import requests
from typing import Any

from local_ai_assistant.llm.clients.ollama import OllamaClient
from local_ai_assistant.config.llm import LLMConfig
from local_ai_assistant.llm.base import BaseLLMClient


class FakeObject:

    def raise_for_status(self):
        pass

    def json(self):
        return {"response": "test"}


def fake_post(*args: Any, **kwargs: Any) -> FakeObject:
    return FakeObject()


def fake_error(*args: Any, **kwargs: Any) -> None:
    raise requests.exceptions.ConnectionError()


@pytest.fixture
def ollama_client() -> BaseLLMClient:
      
    llm_config = LLMConfig(
        provider="ollama",
        model="test-model",
        base_url="test-url",
)

    return OllamaClient(llm_config)  


def test_generate_response(
    monkeypatch: pytest.MonkeyPatch, 
    ollama_client: BaseLLMClient,
    ):

    monkeypatch.setattr(requests, "post", fake_post)

    response = ollama_client.generate_response("hello")

    assert response == "test"


def test_connection_error(
    monkeypatch: pytest.MonkeyPatch,
    ollama_client: BaseLLMClient,
    ):

    monkeypatch.setattr(requests, "post", fake_error)

    with pytest.raises(ConnectionError):
        ollama_client.generate_response("hello")


class FakeHTTPError:

    def raise_for_status(self):
        raise requests.exceptions.HTTPError()


def fake_http_error(*args: Any, **kwargs: Any) -> FakeHTTPError:
    return FakeHTTPError()


def test_http_error(
    monkeypatch: pytest.MonkeyPatch,
    ollama_client: BaseLLMClient,
    ):

    monkeypatch.setattr(requests, "post", fake_http_error)

    with pytest.raises(requests.exceptions.HTTPError):
        ollama_client.generate_response("hello")


