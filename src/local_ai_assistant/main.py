from local_ai_assistant.utils.logger import logger
from local_ai_assistant.llm.factory import get_llm_client
from local_ai_assistant.config.llm import llm_config
from local_ai_assistant import exceptions
from local_ai_assistant.conversation.manager import ConversationManager
from local_ai_assistant.conversation.history import ConversationHistory


try:
    client = get_llm_client(llm_config) 
    logger.info("Local AI Assistant started!")
except exceptions.InvalidLLMProviderError as e:
    print(e)
    exit()

history_messages = ConversationHistory()
manager = ConversationManager(history_messages)

while True:

    print('\nType a message or type "exit" to close the conversation')
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break

    if not user_input.strip():
        print("Please input a prompt")
        continue
    logger.debug("User prompt received")

    ConversationManager.process_user_message(manager, user_input)
    
    logger.debug(f"Content added into history '{history_messages.get_history()}'")

    try:
        response = client.generate_response(history_messages.history_to_str())
        print(f'AI: {response}')

        ConversationManager.process_assistant_message(manager, response)
        
        print(history_messages.history_to_str())
    except exceptions.BaseLLMError as e:
        print(e)

    '''
    for chunk in client.stream_response(user_input):
        print(f"chunks: {chunk}")
    '''