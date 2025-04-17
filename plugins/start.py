from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

# MongoDB connection
mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client["Word"]["WordDb"]

async def create_index():
    """Ensure index exists on 'word' field for faster queries."""
    await db.create_index([("word", 1)])
    print("✅ Index created on 'word' field.")

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    # Create index before sending response
    await create_index()

    user = message.from_user.first_name
    await message.reply_photo(
        photo="https://te.legra.ph/file/fancy-start-image.jpg",
        caption=(
            f"**Hey {user}!**\n\n"
            "I'm a **fun & smart chatbot**.\n"
            "Just type anything or reply to my messages to teach me new things!"
        ),
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Support", url="https://t.me/RU_DRA_098"),
                InlineKeyboardButton("Owner", url="https://t.me/RU_DRA_098")
            ]
        ])
    )
