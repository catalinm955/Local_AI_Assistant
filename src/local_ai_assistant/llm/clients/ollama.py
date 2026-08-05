import requests
from collections.abc import Iterator
import json
from typing import Any

from local_ai_assistant.utils.logger import logger
from local_ai_assistant.llm.base import BaseLLMClient
from local_ai_assistant.config.llm import LLMConfig


class OllamaClient(BaseLLMClient):

    def __init__(self, llm_config: LLMConfig):
        self.model = llm_config.model
        self.base_url = llm_config.base_url


    def stream_response(self, prompt: str) -> Iterator[str]:
        payload: dict[str, str | bool] = {
            "model": self.model,
            "prompt": prompt,
            "stream": True
        }

        try:
            response = requests.post(
                url=self.base_url,
                json=payload,
                stream=True
            )
        except requests.exceptions.ConnectionError as e:
            logger.error("Cannot connect to Ollama")
            raise ConnectionError("Cannot connect to Ollama") from e

        response.raise_for_status()

        logger.info("Receiving streamed response chunks...")

        for chunk in response.iter_lines():
            text: str = chunk.decode("utf-8")
            data: dict[str, Any] = json.loads(text)
            response_text: str = data.get("response", "")

            if response_text:
                yield response_text

            if data.get("done"):
                break


    def generate_response(self, prompt: str) -> str:
        payload: dict[str, str | bool] = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        logger.info(f'Sending request to Ollama (model={self.model})')

        try:
            response = requests.post(
                url=self.base_url,
                json=payload
            )
            
        except requests.exceptions.ConnectionError as e:
            logger.error("Cannot connect to Ollama")
            raise ConnectionError("Cannot connect to Ollama") from e

        response.raise_for_status()

        return response.json()['response']

