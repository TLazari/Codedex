import discord, os, asyncio
from dotenv import load_dotenv
from utils import get_meme, gpt, wiki

load_dotenv()

historico = []
gpt_task = None

async def gpt_timer(historico_ref):
    await asyncio.sleep(30)  
    historico_ref.clear()
    print("⏳ Histórico chat gpt apagado após 5 minutos sem interação.")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} está online!')

    
    async def on_message(self, message):
        
        global gpt_task  
        # ignora msg própria
        if message.author == self.user:
            return
        
        if message.content.startswith('/meme'):
            await message.channel.send(get_meme())
            return
        elif message.content.startswith('/wiki'):
            await message.channel.send(wiki(message.content[5:].strip()))
            print (message.content[5:].strip())
            return
        elif 'helix' in message.content.lower():
            texto = message.content.replace('helix', '').strip()
            pergunta = gpt(texto, historico)
            await  message.channel.send(pergunta)
            historico.append({"role": "user", "content": texto})
            historico.append({"role": "assistant", "content": pergunta})
            if gpt_task:
                gpt_task.cancel()
            gpt_task = asyncio.create_task(gpt_timer(historico))
            
            return

intents = discord.Intents.default()
intents.message_content = True #Interagir por mensagem

botKey = os.getenv('botKeyDC')
client = MyClient(intents=intents)
client.run(botKey)

