# Using this file to learn discord.py
# This example requires the 'message_content' intent.

import os
import discord
import logging
from dotenv import load_dotenv

load_dotenv()

client_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Assume client refers to a discord.Client subclass...
client.run(client_token, log_handler=handler, log_level=logging.DEBUG)

