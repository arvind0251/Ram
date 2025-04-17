from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/fancy-start-image.jpg",  # Add your image
        caption="**Hey! I'm a fun chatbot. Just talk to me or reply to my messages to teach me!**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Support", url="https://t.me/RU_DRA_098")],
            [InlineKeyboardButton("Owner", url="https://t.me/RU_DRA_098")],
        ])
    )
