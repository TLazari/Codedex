import openai, os, wikipedia,json, requests
from dotenv import load_dotenv
from wikipedia.exceptions import DisambiguationError, PageError


wikipedia.set_lang("pt")
def wiki(message):
    try:
      texto = wikipedia.summary(message, sentences = 5)
      if len(texto) > 2000:
        return texto[:1997] + "..."  
      return texto
    
    except DisambiguationError as e:
      opcoes = e.options[:5]  # Pega só as 5 primeiras sugestões
      sugestoes = '\n'.join(f"- {op}" for op in opcoes)
      return f"🔍 Sua busca foi ambígua. Tente ser mais específico. Algumas sugestões:\n{sugestoes}"
    
    except PageError:
        return "❌ Nenhuma página encontrada com esse nome."
    
    except Exception as e:
      if len(e) > 2000:
        return f"⚠️ Ocorreu um erro: {e[:1997]}" 
    


def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']


load_dotenv()
chatGptKey = os.getenv('chatGptKey') #Api do .env
openai.api_key = chatGptKey 

def gpt (message, historico):
    historico_limitado = historico [-5*2:]
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {chatGptKey}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",         
        "messages": [
            {"role": "system", "content": "Você é um assistente útil, educado e sempre responde em pt-br, e lembre que está respondendo pelo discord por tanto use."},
            ] + historico_limitado + [ 
            {"role": "user", "content": message}
        ],
        "temperature": 0.7,
        "max_tokens": 400
    }
    response = requests.post(url, headers=headers, json=data)
    resposta = response.json()
    resposta = resposta['choices'][0]['message']['content']
    return resposta
