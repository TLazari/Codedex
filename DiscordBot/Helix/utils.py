import openai, os, wikipedia
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
    

load_dotenv()
chatGptKey = os.getenv('chatGptKey') #Api do .env
openai.api_key = chatGptKey 


def gpt(message,contexto):

  prompt = f'{contexto} + {message}'
  resposta = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = prompt, 
    max_tokens = 400,
    temperature = 0.3
  )
  retorno_gpt = resposta.choices[0].text.strip()
  contexto += f'usuário input: {message}\n Assistente: {retorno_gpt}' 
  print (retorno_gpt)
  return retorno_gpt

