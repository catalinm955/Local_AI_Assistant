from local_ai_assistant.conversation.message import Message


class ConversationHistory:
    def __init__(self):
        self.messages: list[Message] = []

    def add_message(self, message: Message):
        self.messages.append(message)

    def get_history(self) -> list[Message]:
        return self.messages