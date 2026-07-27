from dataclasses import dataclass


@dataclass
class LLMConfig:
    provider: str
    model: str
    base_url: str
    api_key: str | None = None


llm_config = LLMConfig(
    provider="ollama",
    model="qwen2.5:1.5b",
    base_url="http://localhost:11434/api/generate",
)