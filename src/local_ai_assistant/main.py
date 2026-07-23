from local_ai_assistant.llm.ollama import generate_response

while True:
    user_input = input("You: ")
    response = generate_response(user_input)
    print(f'AI: {response}')