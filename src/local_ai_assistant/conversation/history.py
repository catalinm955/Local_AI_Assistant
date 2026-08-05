from local_ai_assistant.conversation.message import Message


class ConversationHistory:
    def __init__(self):
        self.messages: list[Message] = []

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def get_history(self) -> list[Message]:
        return self.messages

    def history_to_str(self) -> str:
        conversation_string: str = ""
        for message in self.messages:
            role = message.role.value
            content = message.content
            conversation_string += role + ": " + content + "; "

        return conversation_string