from enum import Enum
from dataclasses import dataclass


class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"


@dataclass(frozen=True)
class Message:
    role: Role
    content: str