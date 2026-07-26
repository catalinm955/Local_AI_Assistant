from abc import ABC, abstractmethod


class BaseLLMClient(ABC):
    
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        ...