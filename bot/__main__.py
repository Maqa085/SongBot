import os
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot.plugins"),
)

if __name__ == "__main__":
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    
    print("Bot başladılır...")
    app.start()
    print(f"@{app.get_me().username} İşləyir!")
    idle()
    app.stop()
    
