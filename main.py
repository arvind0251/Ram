from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import asyncio
import logging
import os

logging.basicConfig(level=logging.INFO)

plugins = dict(root="plugins")

app = Client(
    "chatbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins
)

if __name__ == "__main__":
    app.run()
