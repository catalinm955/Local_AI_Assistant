from local_ai_assistant.utils.logger import logger
from local_ai_assistant.llm.factory import get_llm_client
from local_ai_assistant.config.llm import llm_config
from local_ai_assistant import exceptions


try:
    client = get_llm_client(llm_config) 
    logger.info("Local AI Assistant started!")
except exceptions.InvalidLLMProviderError as e:
    print(e)
    exit()

while True:

    print('\nType a message or type "exit" to close the conversation')
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break

    if not user_input.strip():
        print("Please input a prompt")
        continue
    logger.debug("User prompt received")

    try:
        response = client.generate_response(user_input)
        print(f'AI: {response}')
    except exceptions.BaseLLMError as e:
        print(e)
