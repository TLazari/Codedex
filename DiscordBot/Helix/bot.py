import discord, os
from dotenv import load_dotenv
from utils import get_meme, gpt, wiki

load_dotenv()

historico = []

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} está online!')
    
    async def on_message(self, message):
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
            print (texto)
            pergunta = gpt(texto, historico)
            print (pergunta)
            await  message.channel.send(pergunta)
            historico.append({"role": "user", "content": texto})
            historico.append({"role": "assistant", "content": pergunta})
            print (historico)
            return

intents = discord.Intents.default()
intents.message_content = True #Interagir por mensagem

botKey = os.getenv('botKeyDC')
client = MyClient(intents=intents)
client.run(botKey)

