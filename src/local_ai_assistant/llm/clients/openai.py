from local_ai_assistant.llm.base import BaseLLMClient
from local_ai_assistant.utils.logger import logger
import requests


class OpenAIClient(BaseLLMClient):

    def __init__(self, config: dict[str, str]):
        self.model = config["model"]
        self.base_url = config["base_url"]
        self.api_key = config["api_key"]

    def generate_response(self, prompt: str) -> str:
        payload: dict[str, str  | bool] = {
            "model": self.model,
            "prompt": prompt,
            "stream": False 
        }    

        logger.info(f"Sending request to OpenAI (model={self.model})")

        try:
            response = requests.post(
                url=self.base_url,
                json=payload
            )
        except requests.exceptions.ConnectionError as e:
            logger.error("Cannot connect to OpenAI")
            raise ConnectionError("Cannot connect to OpenAI") from e

        response.raise_for_status()

        return response.json()["response"]
