import requests
import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def fetch_tech_article():
    url = 'https://zenn-api.netlify.app/trendTech.json'
    r = requests.get(url)
    responses = r.json()
    article_urls = []
    for response in responses:
        article_urls.append("https://zenn.dev" + response["path"])
    return article_urls

async def fetch_sent_messages():
    sent_messages = []
    channel = client.get_channel(1072507059322507327)
    async for message in channel.history():
        if message.author == client.user:
            sent_messages.append(message.content)
    
    return sent_messages


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('fetch'):
        article_urls = fetch_tech_article()
        sent_messages = await fetch_sent_messages()
        diff_article_urls = list(set(article_urls) - set(sent_messages))
        if not diff_article_urls:
            await message.channel.send("新規の記事はないよ")
            return
        for url in diff_article_urls:
            await message.channel.send(url)

client.run(os.getenv("TOKEN"))
