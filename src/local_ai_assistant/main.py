from local_ai_assistant.llm.clients.ollama import generate_response
from local_ai_assistant.utils.logger import logger

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
        response = generate_response(user_input)
        print(f'AI: {response}')
    except ConnectionError as e:
        print(e)