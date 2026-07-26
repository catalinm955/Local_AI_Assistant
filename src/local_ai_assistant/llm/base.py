from abc import ABC, abstractmethod


class BaseLLMClient(ABC):

    def __init__(self, config: dict[str, str]):
        ...

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        ...