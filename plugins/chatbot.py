import random, re, logging
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

db = AsyncIOMotorClient(MONGO_URL)["Word"]["WordDb"]
UNWANTED_REGEX = r"^[\W_]+$|[\/!?\~\\]"

@Client.on_message(filters.text & ~filters.bot)
async def chatbot(client, message: Message):
    if re.match(UNWANTED_REGEX, message.text):
        return

    if message.chat.type in ["private", "group"]:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

    responses = await db.find({"word": message.text}).to_list(length=10)

    if message.reply_to_message:
        if message.reply_to_message.from_user.id == (await client.get_me()).id:
            if responses:
                r = random.choice(responses)
                await message.reply_sticker(r["text"]) if r["check"] == "sticker" else await message.reply_text(r["text"])
        else:
            if message.text:
                await db.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "text"})
            elif message.sticker:
                await db.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker"})
    else:
        if responses:
            r = random.choice(responses)
            await message.reply_sticker(r["text"]) if r["check"] == "sticker" else await message.reply_text(r["text"])
