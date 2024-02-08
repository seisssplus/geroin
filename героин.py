from pyrogram import Client, filters
from pyrogram.types import Message
import time
import asyncio
import psutil
import random
from datetime import datetime, date, timedelta
import aiofiles
import pytz
from pathlib import Path
from pyrogram.errors import FloodWait
import sympy
from io import BytesIO 


api_id = 23962937
api_hash = 'e247a38e5d7d45235018717e76920252'
app = Client('client', api_id, api_hash)
start_time = time.time()




#############################################СРОЛЬ КОМАНДЫ########
#############################

@app.on_message(filters.command("ebatl", prefixes=".") & filters.me)
async def speral_command(client, message):
    args = message.text.split()[1:]
    delay = int(args[0])
    duration = int(args[1])
    
    with open("video.txt", "r") as file:
        video_link = file.readline().strip()

    with open("x3.txt", "r") as file:
        messages = file.readlines()
    num_messages = len(messages)
    total_delay = delay * num_messages
    num_loops = duration // total_delay   
    await message.edit_text("† ϰαɥμϰα϶ ραӡρƅɞατɩ εδλσϲσσσϲƅ ϰεɠσϰσωεϰƅχ ϲƅϰσӄσɞ δλબɠµτɞαρεύ ϲɞσμϻ δσӷσχγεϻ †")
    
    for _ in range(num_loops):
        for text in messages:
            await send_video_with_text(message.chat.id, video_link, text.strip())
            await asyncio.sleep(delay)
    
    remaining_duration = duration % total_delay
    remaining_messages = (remaining_duration // delay) if remaining_duration > delay else 1
    for text in messages[:remaining_messages]:
        await send_video_with_text(message.chat.id, video_link, text.strip())
        await asyncio.sleep(delay)

async def send_video_with_text(chat_id, video_link, text):
    await app.send_video(chat_id, video_link, caption=text)


@app.on_message(filters.command("grn", prefixes=".") & filters.me)
async def speral_command(client, message):
    args = message.text.split()[1:]
    delay = int(args[0])
    duration = int(args[1])
    additional_text = " ".join(args[2:])
    await message.edit_text("✶ ɞκ૦ʌ૦ʌ ɾ૯ƿ૦ⲏɑ ɞ ੮ɞ૦ю ⲙɑ੮ƴⲭƴ ɑ ૦ⲏɑ ਡ∂૦ⲭʌɑ ⲏɑⲭƴύ. ✶")

    with open("x.txt", "r", encoding="utf8") as file:
        messages = file.readlines()
    num_loops = duration // (len(messages) * max(delay, 1))
    for _ in range(num_loops):
        await send_messages(message.chat.id, messages, delay, additional_text)
    remaining_duration = duration % (len(messages) * max(delay, 1))
    await send_messages(message.chat.id, messages[:remaining_duration // max(delay, 1)], delay, additional_text)

async def send_messages(chat_id, messages, delay, additional_text=""):
    for message in messages:
        await app.send_message(chat_id, additional_text + message.strip())
        await asyncio.sleep(delay)


@app.on_message(filters.command("shpric", prefixes=".") & filters.me)
async def speral_command(client, message):
    args = message.text.split()[1:]
    delay = int(args[0])
    duration = int(args[1])

    with open("photo.txt", "r", encoding="utf8") as file:
        photo_link = file.readline().strip() 

    with open("x3.txt", "r", encoding="utf8") as file:
        messages = file.readlines()
    num_messages = len(messages)
    total_delay = delay * num_messages
    num_loops = duration // total_delay
    await message.edit_text("𖤐 ɞӄαλƅɞα϶ ωηρμҵ ɞ τελɩҵε ϻατερεύ ϰεɠσϰσωεϰϰƅχ ϲƅϰσϲɞμϰϲτγϲσɞ. 𖤐")

    for _ in range(num_loops):
        for text in messages:
            await app.send_photo(message.chat.id, photo_link, caption=text.strip())
            await asyncio.sleep(delay)
    
    remaining_duration = duration % total_delay
    remaining_messages = (remaining_duration // delay) if remaining_duration > delay else 1
    for text in messages[:remaining_messages]:
        await app.send_photo(message.chat.id, photo_link, caption=text.strip())
        await asyncio.sleep(delay)


@app.on_message(filters.command("vkal", prefixes=".") & filters.me)
async def speral_command(client, message):
    args = message.text.split()[1:]
    delay = int(args[0])
    duration = int(args[1])
    additional_text = " ".join(args[2:])
    await message.edit_text("✶ ⲃⲕⲁⲗыⲃⲁю ⲇⲟⳅⲩ ⲃ ⲃⲉⲏы ⲇⲉⲧυⲱⲉⲕ ⳝⲗяⲇⲉύ ✶")

    with open("x2.txt", "r", encoding="utf8") as file:
        messages = file.readlines()
    num_loops = duration // (len(messages) * max(delay, 1))
    for _ in range(num_loops):
        await send_messages(message.chat.id, messages, delay, additional_text)
    remaining_duration = duration % (len(messages) * max(delay, 1))
    await send_messages(message.chat.id, messages[:remaining_duration // max(delay, 1)], delay, additional_text)

async def send_messages(chat_id, messages, delay, additional_text=""):
    for message in messages:
        await app.send_message(chat_id, additional_text + message.strip())
        await asyncio.sleep(delay)

@app.on_message(filters.me & filters.command("lsnk", prefixes="."))
def lesenk_command(client, message):
    text = message.text.split()[1:]
    message.delete()
    for word in text:
        client.send_message(chat_id=message.chat.id, text=word)


@app.on_message(filters.me & filters.command("lsnka", prefixes="."))
async def lesenk_command(client, message):
    args = message.text.split()[1:]
    word_count = int(args[0]) if args else 1
    with open("x4.txt", "r", encoding="utf-8") as file:
        words = file.read().split()
    if word_count > len(words):
        word_count = len(words)
    selected_words = random.sample(words, word_count)
    output_text = " ".join(selected_words)
    await message.edit_text(f"{args[1]} {output_text}") 

###############################################ХЕЛПЫ#################################

@app.on_message(filters.me & filters.command("героин", prefixes="."))
def astehelp(client, message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username
    username = message.from_user.username
    message.edit("†")
    message.delete()
    client.send_photo(chat_id=message.chat.id, photo="https://te.legra.ph/file/7612a2d623ce46db67b6d.jpg", caption=f"""
**༒ ⳜⲞⲦ ⲎⲀ ⲀⲔⲔ ⲄⲈⲢⲞⳘⲎ ༒**

**➪ Дата первого релиза:** <code>12 дек. | 2023</code>
**➪ Дата идеи юба:** <code>11 дек. 23:43:31 | 2033</code>
**➪ Дата выпускал в имп:** <code>16 дек. | 2023</code>
**➪ Нынешнее обнолвнение:** <code>2.9</code>

**➫ Хелпы:** <code>.ghlp</code> | <code>.ghlp2</code>

**➮ Дев. разраб -** <code>i_seis.t.me</code>
__В разработке участвовало количкство людей: <code>1</code>.__
 """)

@app.on_message(filters.me & filters.command("ghlp", prefixes="."))
def astehelp(client, message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username
    username = message.from_user.username
    message.edit("💉💉")
    message.edit("💉 ૦੮κƿыɞɑю 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη  💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ ⲙɑʌ૯ⲏьκυⲭ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ ⲙɑʌ૯ⲏьκυⲭ ςыⲏ૦κ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ ⲙɑʌ૯ⲏьκυⲭ ςыⲏ૦κ ɞਡ∂ы੮ыκ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ ⲙɑʌ૯ⲏьκυⲭ ςыⲏ૦κ ɞਡ∂ы੮ыκ ઠʌя∂૯ύ. 💉")
    message.delete()
    client.send_message(
        chat_id=message.chat.id,
        text=f"""
1 ⲗυⲥⲧ ⲕⲟⲙⲁⲏⲇ:

✶ <code>.shpric</code> + ⲕⲇ + ⲥⲕⲟⲕ. ⲥⲗⲟⲃ + юⳅ/υⲇ - ⲏⲟⲏ ⲥⲧⲟⲡ ⲥ ⲫⲟⲧⲟ.
✶ <code>.ebatl</code> + ⲕⲇ + ⲥⲕⲟⲕ. ⲥⲗⲟⲃ + юⳅ/υⲇ - ⲏⲟⲏ ⲥⲧⲟⲡ ⲥ ⲃυⲇⲉⲟ.
✶ <code>.lsnk</code> + ⲧⲉⲕⲥⲧ - ⲉⳝⲁⲱυⲧ ⲗⲉⲥⲉⲏⲕⲩ.
✶ <code>.lsnka</code> + ⳡυⲥⲗⲟ ⲥⲕⲟⲕ. ⲥⲗⲟⲃ - ⲣⲁⲏⲇⲟⲙⲏⲟ ⲃыⲃⲟⲇυⲧ ⲗⲉⲥⲉⲏⲕⲟύ ⲧⲉⲕⲥⲧ ⲥ ⲫⲁύⲗⲁ.
✶ <code>.grn</code> + ⲕⲇ + ⲥⲕⲟⲕ. ⲥⲗⲟⲃ + юⳅ/υⲇ - ⲇⲉⲫⲟⲗⲧ ⲏⲟⲏ ⲥⲧⲟⲡ.
✶ <code>.vkal</code> + ⲕⲇ + ⲥⲕⲟⲕ. ⲥⲗⲟⲃ + юⳅ/υⲇ - ⲇⲉⲫⲟⲗⲧ ⲏⲟⲏ ⲥⲧⲟⲡ.
†──▸◂─†─▸◂──†

✶ 𝙲𝙰𝚁𝚁𝙸𝙴𝚁: <code>{name}</code>
✶ 𝙸𝙳: <code>@{user_id}</code>
✶ 𝙽𝙰𝙼𝙴: <code>{name}</code>
✶ 𝚄𝚂𝙴𝚁: <code>@{username}</code>
✶ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <code>#сеис, #psycholitic</code>
 """)


@app.on_message(filters.me & filters.command("ghlp2", prefixes="."))
def astehelp(client, message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username
    username = message.from_user.username
    message.edit("💉💉")
    message.edit("💉 ૦੮κƿыɞɑю 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη  💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ ⲙɑʌ૯ⲏьκυⲭ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ ⲙɑʌ૯ⲏьκυⲭ ςыⲏ૦κ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ ⲙɑʌ૯ⲏьκυⲭ ςыⲏ૦κ ɞਡ∂ы੮ыκ 💉")
    message.edit("💉 ૦੮κƿыɞɑю ⲭ૯ʌη η૦ƿ૦ж∂ɑю ɞ κƿ૦ɞυ ਘʌюਘⲏыⲭ ⲙɑ੮૯ƿ૯ύ ⲙɑʌ૯ⲏьκυⲭ ςыⲏ૦κ ɞਡ∂ы੮ыκ ઠʌя∂૯ύ. 💉")
    message.delete()
    client.send_message(
        chat_id=message.chat.id,
        text=f"""
2 ⲗυⲥⲧ ⲕⲟⲙⲁⲏⲇ:

† <code>.slov</code> - ⲥⳡυⲧыⲃⲁⲉⲧ ⲕⲟⲗυⳡⲉⲥⲧⲃⲟ ⳝⲩⲕⲃ ⲃ ⲥⲗⲟⲃⲉ.
† <code>.leave</code> - ⲗυⲃⲏⲩⲧь ⲥ ⲕⲫ.
† <code>.героин</code> - υⲏⲫ ⲟ юⳝⲉ.
† <code>.cl</code> - ⲡυⲱυⲧⲉ ⲡⲣυⲙⲉⲣ ⲏⲁ ⲕⲟⲧⲟⲣыύ ⲭⲟⲧυⲧⲉ ⲟⲧⲃⲉⲧ.
† <code>.spm</code> + ⲥⲕⲟⲕ. ⲥⲗⲟⲃ + ⳅⲁⲇⲉⲣⲯⲕⲁ ⲃ ⲥⲉⲕ. + ⲧⲉⲕⲥⲧ - ⲉⳝⲁⲱυⲧ ⲥⲡⲁⲙ ⲥ ⳅⲁⲇⲉⲣⲯⲕⲟύ.
† <code>.cf</code> - ⳡⲉⲕⲏⲩⲧь υⲏⲫⲩ ⲟ ⲅⲣⲩⲡⲡⲉ
† <code>.ping</code> - ⳡⲉⲕ ⲡυⲏⲅ ⲁ ⲙⲥ.
† <code>.uptime</code> - ⳡⲉⲕⲏⲩⲧь ⲁⲡⲧⲁύⲙ.
† <code>.id</code> - ⳡⲉⲕⲏⲩⲧь ⲥⲃⲟύ υⲇ. - ⲣⲉⲡⲗ ⳡⲉⲗⲩ ⳡⲧⲟⳝы ⳡⲉⲕⲏⲩⲧь ⲉⲅⲟ υⲇ.
† <code>.idc</code> - ⳡⲉⲕⲏⲩⲧь υⲇ ⲕⲫ.

†──▸◂─†─▸◂──†

✶ <code>.gc</code> - ⲏⲉύⲙ ⳅⲁⲙⲉⲧⲕυ + ⲡⲉⲣⲉⲭⲟⲇ ⲏⲁ ⲥⲗⲉⲇ ⲥⲧⲣⲟⲕⲩ + ⲧⲉⲕⲥⲧ.
✶ <code>.gl</code> - ⳡⲉⲕⲏⲩⲧь ⲗυⲥⲧ .ⲧⲕⲧ ⳅⲁⲙⲉⲧⲟⲕ υ ⲧⲇ.
✶ <code>.del</code> + ⲏⲉύⲙ ⳅⲁⲙⲉⲧⲕυ - ⲩⲇⲁⲗυⲧ ⳅⲁⲙⲉⲧⲕⲩ.
✶ <code>.ww</code> + ⲏⲉύⲙ ⳅⲁⲙⲉⲧⲕυ - ⲃыⲃⲉⲥⲧυ ⲧⲉⲕⲥⲧ υⳅ ⳅⲁⲙⲉⲧⲕυ.

†──▸◂─†─▸◂──†

✶ 𝙲𝙰𝚁𝚁𝙸𝙴𝚁: <code>{name}</code>
✶ 𝙸𝙳: <code>@{user_id}</code>
✶ 𝙽𝙰𝙼𝙴: <code>{name}</code>
✶ 𝚄𝚂𝙴𝚁: <code>@{username}</code>
✶ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <code>#сеис, #psycholitic</code>
""")

###############################################ЗАМЕТКИ#################################

@app.on_message(filters.me & filters.command("gc", prefixes="."))
async def create_file(client, message):
    try:
        args = message.text.split(maxsplit=1)[1].split(maxsplit=1)
        file_name = args[0]
        file_text = args[1]

        file_path = Path("") / f"{file_name}.txt"
        async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
            await f.write(file_text)

        await message.reply(f"† ⳅⲁⲙⲉⲧⲕⲁ ⲥⲟⳅⲇⲁⲏⲁ.")
        await message.delete()
    except Exception as e:
        await message.reply(f"Ошибка: {e}")



@app.on_message(filters.command("gl", prefixes=".") & filters.me)
async def show_files_and_folders(client, message):
    try:
        folder_path = Path(".")
        files = [f.name for f in folder_path.iterdir() if f.is_file() and f.name.endswith(".txt") and f.name not in ["x.txt", "x2.txt", "x3.txt", "x4.txt"]]
        file_list = "\n".join([f"• <code>{f}</code>" for f in files]) if files else "ⲏⲉⲧ ⲫⲁύⲗⲟⲃ ⲥ ⳅⲁⲙⲉⲧⲕⲟύ."

        await message.reply(f"† ⲥⲡυⲥⲟⲕ .ᴛxᴛ †\n\n{file_list}")
        await message.delete()
    except Exception as e:
        await message.reply(f"Ошибка: {e}")



@app.on_message(filters.command("del", prefixes=".") & filters.me)
async def delete_file(client, message):
    try:
        _, file_to_delete = message.text.split(maxsplit=1)
        file_to_delete = file_to_delete.strip()
        file_path = Path(".") / file_to_delete
        
        if file_path.is_file():
            file_path.unlink()
            await message.reply(f"† ⳅⲁⲙⲉⲧⲕⲁ {file_to_delete} ⲩⲇⲁⲗⲉⲏⲁ.")
        else:
            await message.reply(f"ⳅⲁⲙⲉⲧⲕⲁ ⲏⲉ ⳝыⲗⲁ ⲏⲁύⲇⲉⲏⲁ.")
            await message.delete()
    except Exception as e:
        await message.reply(f"Ошибка: {e}")


@app.on_message(filters.command("ww", prefixes=".") & filters.me)
async def show_file_text(client, message):
    try:
        _, file_name = message.text.split(maxsplit=1)
        file_path = Path(".") / file_name
        
        if file_path.is_file():
            async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
                file_text = await f.read()
            await message.reply(f"ⲧⲉⲕⲥⲧ ⳅⲁⲙⲉⲧⲕυ {file_name}:\n\n{file_text}")
        else:
            await message.reply(f"ⳅⲁⲙⲉⲧⲕⲁ ⲏⲉ ⳝыⲗⲁ ⲏⲁύⲇⲉⲏⲁ.")
    except Exception as e:
        await message.reply(f"Ошибка: {e}")

###############################################ХУЙНЯ####################################


@app.on_message(filters.me & filters.command("leave", prefixes="."))
def leave_group(client, message):
    user_text = message.text.split(maxsplit=1) 
    chat_id = message.chat.id
    chat_title = message.chat.title
    user_id = message.from_user.id

    if len(user_text) > 1:
        leave_text = user_text[1] 
        leave_message = f"ⲗυⲃ ⲥ ⲅⲣⲩⲡⲡы.\nⲥ ⲥⲗⲟⲃⲁⲙυ: <code>{leave_text}</code>"
    else:
        leave_message = f"ⲗυⲃ ⲥ ⲅⲣⲩⲡⲡы."

    client.send_message(
        chat_id=chat_id,
        text=leave_message
    )
    client.leave_chat(chat_id)

@app.on_message(filters.command('slov', prefixes='.') & filters.me)
def kol(_, msg):
    chethik_slov = msg.reply_to_message.text.split(' ')
    ottf = len(chethik_slov)
    jkjj = int(ottf-1)
    msg.edit(f"ⲥⲗⲟⲃ: {jkjj}")

@app.on_message(filters.command("spm", prefixes=".") & filters.me)
async def send_multiple_messages(client, message):
    try:
        _, count, delay, text = message.text.split(maxsplit=3)
        count = int(count)
        delay = int(delay)
        for _ in range(count):
            await message.reply(text)
            await asyncio.sleep(delay)
            await message.delete()
    except Exception as e:
        await message.reply(f"Ошибка: {e}")

@app.on_message(filters.me & filters.command("uptime", prefixes="."))
async def get_uptime(client, message):
    current_time = time.time()
    uptime_seconds = int(current_time - start_time)
    await message.reply_text(f"✶ᴜᴘᴛɪᴍᴇ: <code>{uptime_seconds} s</code>")
    await message.delete()


@app.on_message(filters.command("uid", prefixes="."))
def uid_command(client, message):

    chat = client.get_chat(message.chat.id)
    chat_title = chat.title
    members = client.get_chat_members(message.chat.id)

    ids_text = f" \"{chat_title}\":\n"
    for member in members:
        user_id = member.user.id
        username = member.user.username
        name = member.user.first_name if member.user.first_name else ""
        nickname = f"{name} [{user_id}] @{username}" if username else f"{name} [{user_id}]"
        ids_text += f"{nickname}\n\n"

    if len(ids_text) > 1:
        file_data = BytesIO(ids_text.encode("utf-8"))
        file_data.name = "popa.txt"
        client.send_document(message.chat.id, file_data, caption="список в файле popa.txt")
    else:
        message.reply_text(ids_text, quote=True)
        message.delete()


@app.on_message(filters.me & filters.command("ping", prefixes="."))
async def ping(client, message):
    start = time.time()
    msg = await message.reply("†")
    end = time.time()
    duration_ms = (end - start) * 1000
    await msg.edit(f"<code>{duration_ms:.2f} ϻϲ</code>")
    await message.delete()


@app.on_message(filters.me & filters.command("cf", prefixes="."))
async def group_info_command(client, message):
    chat = await client.get_chat(message.chat.id)

    group_info_text = f"✶ɪᴅ ᴄʜᴀᴛ: <code>{chat.id}</code>\n✶ɴᴀᴍᴇ: <code>{chat.title}</code>\n"

    if chat.username:
        group_info_text += f"✶ᴜsᴇʀ-ɴᴀᴍᴇ: <code>@{chat.username}</code>\n"

    chat_info = await client.get_chat_members_count(chat.id)
    group_info_text += f"✶ᴘᴇᴏᴘʟᴇ: <code>{chat_info}</code>\n"
    
    await client.send_photo(chat.id, "https://te.legra.ph/file/d497b25cb3f1e820d96dc.jpg", caption=group_info_text)
    await message.delete()


@app.on_message(filters.me & filters.command("cl", prefixes="."))
def calculate(client, message):
    try:
        expression = message.text.split(".cl ", maxsplit=1)[1]
        result = sympy.sympify(expression)
        response = f"✶ ᴇxᴀᴍᴘʟᴇ: <code>{expression}</code>\n\n✶ sᴏʟᴜᴛɪᴏɴ: <code>{result}</code>"
        message.reply_text(response)
        message.delete()
    except Exception as e:
        message.reply_text(f"ошибка: {e}") 

@app.on_message(filters.me & filters.text & filters.command("id", prefixes="."))
async def get_user_id(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await message.reply_to_message.reply_text(f"✶ɪᴅ: <code>{user_id}</code> ✶")
        await message.delete()
    else:
        my_id = message.from_user.id
        await message.edit_text(f"✶ɪᴅ: <code>{my_id}</code> ✶")


@app.on_message(filters.me & filters.text & filters.command("idc", prefixes="."))
async def get_chat_id(client, message):
    chat_id = message.chat.id
    await message.edit_text(f"✶ɪᴅ ᴄʜᴀᴛ: <code>{chat_id}</code> ✶")


print("nick")
app.run()