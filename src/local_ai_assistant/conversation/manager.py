from local_ai_assistant.conversation.message import Message, Role
from local_ai_assistant.conversation.history import ConversationHistory
from local_ai_assistant.utils.logger import logger


class ConversationManager:

    def __init__(self, conversation_history: ConversationHistory):
        self.conversation_history = conversation_history

    def process_user_message(self, user_input: str) -> None:
        user_message = Message(
            role=Role.USER,
            content=user_input
        )
        logger.debug("User input converted into content")

        self.conversation_history.add_message(user_message)
        logger.debug("User message added into history")

    def process_assistant_message(self, response: str) -> None:
        assistant_message = Message(
            role=Role.ASSISTANT,
            content = response
        )
        logger.debug("Assistant response converted into content")

        self.conversation_history.add_message(assistant_message)
        logger.debug("Assistant response added into history")