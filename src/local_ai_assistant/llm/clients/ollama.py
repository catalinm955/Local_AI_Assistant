import requests
from local_ai_assistant.utils.logger import logger
from local_ai_assistant.llm.base import BaseLLMClient


class OllamaClient(BaseLLMClient):

    def __init__(self, config: dict[str, str]):
        self.model = config["model"]
        self.base_url = config["base_url"]

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
