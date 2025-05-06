import discord, os, asyncio
from dotenv import load_dotenv
from utils import get_meme, gpt, wiki

load_dotenv()


historico = []
gpt_task = None

async def gpt_timer(historico_ref):
    await asyncio.sleep(300)  
    historico_ref.clear()
    print("⏳ Histórico CHATGPT apagado após 5 minutos sem interação.")

intents = discord.Intents.default()
bot = discord.Bot(intents = intents)


@bot.event
async def on_ready():
    print(f'{bot.user} está online!')

@bot.slash_command(name='meme', description = 'Envia um meme aleatório', guild_ids = [1362846398638194978])
async def meme_command(ctx:discord.ApplicationContext):
    await ctx.respond(get_meme())

@bot.slash_command(name='wiki', description = 'Busca na Wikipedia', guild_ids = [1362846398638194978])
async def wiki_command(ctx:discord.ApplicationContext, termo: str):
    resposta = wiki(termo)
    print(termo)
    await ctx.respond(resposta)

@bot.slash_command(name='helix', description = 'Conversa com a IA Helix', guild_ids = [1362846398638194978])
async def helix_command(ctx:discord.ApplicationContext, pergunta: str):
    global gpt_task
    resposta = gpt(pergunta, historico)
    historico.append({"role": "user", "content": pergunta})
    historico.append({"role": "assistant", "content": resposta})
    await ctx.respond(resposta)

    if gpt_task:
        gpt_task.cancel()
    gpt_task = asyncio.create_task(gpt_timer(historico))
    

botKey = os.getenv('botKeyDC')
bot.run(botKey)


