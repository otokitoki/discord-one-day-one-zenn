from flask import Flask
from threading import Thread
from bot import get_diff_article_urls, client

app = Flask('')


@app.route('/')
async def home():
  diff_article_urls = get_diff_article_urls()
  if not diff_article_urls:
    print("empty diff_article_urls")
  for url in diff_article_urls:
    print(url)
    await client.get_channel(1072507059322507327).send(url)
  return "hello!"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
