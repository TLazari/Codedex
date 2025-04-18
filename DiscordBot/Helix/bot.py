import discord, requests, json, os
from dotenv import load_dotenv
from utils import gpt, wiki


load_dotenv()

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    

    async def on_message(self, message):

        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        if message.content.startswith('oi'):
            await message.channel.send('Olá {0}'.format(message.author))
        if message.content.startswith('/wiki'):
            await message.channel.send(wiki(message.content[5:].strip()))
            print (message.content[5:].strip())
        if message.content.startswith('/chat'):
            await message.channel.send(gpt(message.content))
            print (message)


intents = discord.Intents.default()
intents.message_content = True #Interagir por mensagem

botKey = os.getenv('botKeyDC')
client = MyClient(intents=intents)
client.run(botKey)

