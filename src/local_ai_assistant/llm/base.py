from abc import ABC, abstractmethod
from local_ai_assistant.config.llm import LLMConfig


class BaseLLMClient(ABC):

    def __init__(self, llm_config: LLMConfig):
        ...

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        ...