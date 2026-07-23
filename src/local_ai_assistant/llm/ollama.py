import requests

OLLAMA_URL = 'http://localhost:11434/api/generate'
MODEL_NAME = 'qwen2.5:3b'

def generate_response(prompt):
    payload = {
        'model': MODEL_NAME,
        'prompt': prompt,
        'stream': False
    }
    try:
        response = requests.post(
            url = OLLAMA_URL,
            json = payload
        )
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Cannot connect to Ollama")

    response.raise_for_status()

    return response.json()['response']
