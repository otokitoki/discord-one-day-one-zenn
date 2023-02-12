import os
from dotenv import load_dotenv
from keep_alive import keep_alive
from bot import client
import discord

load_dotenv()

if __name__ == "__main__":
  try:
    keep_alive()
    client.run(os.getenv("TOKEN"))

  except Exception as e:
    print(e)
    discord.client._log.exception("exception : %s", e)
