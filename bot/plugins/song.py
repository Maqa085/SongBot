import os
import requests
import yt_dlp
from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from bot.translate import EN

@Client.on_message(filters.command("song"))
async def download_song(_, message):
    if len(message.command) < 2:
        return await message.reply("İstifadə: /song mahnı adı")

    query = " ".join(message.command[1:])
    m = await message.reply(EN.SONG_SEARCHING)
    
    ydl_ops = {
        "format": "bestaudio[ext=m4a]",
        "outtmpl": f"downloads/%(title)s.%(ext)s",
        "noplaylist": True,
    }

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results:
            raise Exception("Tapılmadı")
            
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"]
        thumbnail = results[0]["thumbnails"][0]
        duration = results[0]["duration"]
        channel_name = results[0]["channel"]
        
        # Fayl adını təmizləyək
        thumb_name = "thumb.jpg"
        thumb_data = requests.get(thumbnail, allow_redirects=True).content
        with open(thumb_name, "wb") as f:
            f.write(thumb_data)

    except Exception as e:
        await m.edit(EN.SONG_NOT_FOUND)
        return

    await m.edit(EN.SONG_DOWNLOADING)
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            audio_file = ydl.prepare_filename(info_dict)

        # Müddəti saniyəyə çevirək
        dur_arr = duration.split(":")
        dur = sum(int(x) * 60**i for i, x in enumerate(reversed(dur_arr)))

        await m.edit(EN.SONG_UPLOADING)
        await message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=EN.SONG_SEND_SONG.format(title, message.from_user.mention, channel_name),
            duration=dur,
            reply_markup=EN.SONG_BUTTONS,
        )
        await m.delete()
    except Exception as e:
        await m.edit(EN.SONG_ERROR)
        print(f"Xəta: {e}")
    finally:
        if os.path.exists(audio_file): os.remove(audio_file)
        if os.path.exists(thumb_name): os.remove(thumb_name)
        
