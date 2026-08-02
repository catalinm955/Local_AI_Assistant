from enum import Enum
from dataclasses import dataclass


class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"


@dataclass(frozen=True)
class Message:
    role: Role
    content: str

message = Message(
    role=Role.USER,
    content="Hello"
)

print(message)
print(message.role)
print(message.role.value)