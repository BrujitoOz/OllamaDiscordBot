import os
import discord
from discord.ext import commands
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.llms.ollama import Ollama
import logging

# Ollama model name
MODEL = os.getenv("OLLAMA_MODEL_NAME")

# Ollama port
port = os.getenv("OLLAMA_PORT", "11434")
base_url = "http://host.docker.internal"
OLLAMA_BASE_URL = f"{base_url}:{port}"

llm = Ollama(model=MODEL, base_url=OLLAMA_BASE_URL)
chat_engine = SimpleChatEngine.from_defaults(llm=llm)

# Discord
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

async def handle_message(message, user_name):
    if message.content.strip():
        logging.info(f"Message: {message.content.strip()}")
        personalized_content = f"Nombre de usuario: {user_name}\nMensaje: {message.content.strip()}"
        response = await chat_engine.achat(personalized_content)
        logging.info(f"Response: {response}")
        await message.reply(response, mention_author=False)

@bot.event
async def on_ready():
    logging.info(f"{bot.user.name} Ready to chat on Discord!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_name = message.author.display_name

    if isinstance(message.channel, discord.DMChannel):
        await handle_message(message, user_name)

    elif message.reference and message.reference.resolved:
        referenced_message = await message.channel.fetch_message(message.reference.message_id)
        if referenced_message.author == bot.user:
            await handle_message(message, user_name)
            
    elif bot.user.mentioned_in(message):
        await handle_message(message, user_name)

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))