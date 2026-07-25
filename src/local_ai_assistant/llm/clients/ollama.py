import requests
from local_ai_assistant.utils.logger import logger
from local_ai_assistant.config.llm import LLM_CONFIG

class OllamaClient:
    def generate_response(self, prompt):
        payload = {
            'model': LLM_CONFIG["model"],
            'prompt': prompt,
            'stream': False
        }
        logger.info(f'Sending request to Ollama (model={LLM_CONFIG["model"]})')
        try:
            response = requests.post(
                url = LLM_CONFIG["url"],
                json = payload
            )
            
        except requests.exceptions.ConnectionError as e:
            logger.error("Cannot connect to Ollama")
            raise ConnectionError("Cannot connect to Ollama") from e

        response.raise_for_status()

        return response.json()['response']

