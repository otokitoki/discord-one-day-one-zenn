import requests
from replit import db
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_diff_article_urls():
  article_urls = fetch_tech_article()
  save_urls(article_urls)
  sent_messages = db.keys()
  return list(set(article_urls) - set(sent_messages))


def fetch_tech_article():
  url = "https://zenn-api.netlify.app/trendTech.json"
  r = requests.get(url)
  responses = r.json()
  article_urls = []
  for response in responses:
    article_urls.append("https://zenn.dev" + response["path"])
  return article_urls


def save_urls(urls):
  for url in urls:
    db[url] = "article_url"


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  discord.client._log.info("message received: %s", message.content)
  if message.content.startswith("fetch"):
    diff_article_urls = get_diff_article_urls()
    if not diff_article_urls:
      discord.client._log.info("return message: 新規の記事はないよ")
      await message.channel.send("新規の記事はないよ")
      return
    for url in diff_article_urls:
      discord.client._log.info("return message: %s", url)
      await message.channel.send(url)