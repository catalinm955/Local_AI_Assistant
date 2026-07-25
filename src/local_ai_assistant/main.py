from local_ai_assistant.utils.logger import logger
from local_ai_assistant.llm.factory import get_llm_client

client = get_llm_client()
logger.info("Local AI Assistant started!")
while True:

    print('\nType a message or type "exit" to close the conversation')
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break

    if not user_input.strip():
        print("Please input a prompt")
        continue
    logger.info("User prompt received")

    try:
        response = client.generate_response(user_input)
        print(f'AI: {response}')
    except ConnectionError as e:
        print(e)