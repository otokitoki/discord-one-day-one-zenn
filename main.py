import requests
import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


async def fetch_tech():
    url = 'https://zenn-api.netlify.app/trendTech.json'
    r = requests.get(url)
    responses = r.json()
    article_urls = []
    for response in responses:
        article_urls.append("https://zenn.dev" + response["path"])
    print(article_urls)

    channel = client.get_channel(1072507059322507327)
    messages = await channel.history(limit=20)
    # TODO
    print(messages)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await fetch_tech()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('fetch'):
        await fetch_tech()
        

client.run(os.getenv("TOKEN"))
