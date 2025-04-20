import requests, os
from dotenv import load_dotenv

load_dotenv()
chatGptKey = os.getenv('chatGptKey')
API_KEY = chatGptKey



def gpt(message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # ou "gpt-4" se tiver acesso
        "messages": [
            {"role": "user", "content": "Boa noite"}
        ],
        "temperature": 0.7,
        "max_tokens": 400
    }
    response = requests.post(url, headers=headers, json=data)
    resposta = response.json()
    print (resposta)
    resposta = resposta['choices'][0]['message']['content']
    return resposta



print(gpt('boa noite'))
