from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class EN:
    START_WELCOME = "🎶 Hello! I'm a simple Telegram bot.\n🤖 I can download songs for you.\n🎵 Just send me the name of the song."
    SONG_SEARCHING = "🔄 Searching..."
    SONG_NOT_FOUND = "⚠️ No results found."
    SONG_DOWNLOADING = "📥 Downloading..."
    SONG_UPLOADING = "📤 Uploading..."
    SONG_SEND_SONG = "✅ **{}**\n\n👤 Requested by: {}\n📺 Channel: {}"
    SONG_ERROR = "❌ Error occurred."

    START_BUTTONS = InlineKeyboardMarkup([
        [InlineKeyboardButton("👨‍👩‍👧‍👦 XezerFamily", url="https://t.me/XezerFamily"),
         InlineKeyboardButton("🤖 XezerBots", url="https://t.me/XezerBots")],
        [InlineKeyboardButton("👤 Owner", url="https://t.me/xGuliyev")]
    ])

    SONG_BUTTONS = InlineKeyboardMarkup([
        [InlineKeyboardButton("👨‍👩‍👧‍👦 XezerFamily", url="https://t.me/XezerFamily")]
    ])
    
