from pyrogram import Client, filters
from pyrogram.types import Message
from bot.translate import EN

@Client.on_message(filters.command("start") & filters.private)
async def start(_, message: Message):
    await message.reply_text(
        text=EN.START_WELCOME,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=EN.START_BUTTONS,
    )
    
