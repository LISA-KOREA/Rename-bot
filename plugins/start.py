# (C) @LISA_FAN_LK

import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client as Clinton
from config import Config
from pyrogram import Client, filters
from plugins.scripts import Scripted
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert ,find_one
from pyrogram.file_id import FileId
import datetime

currentTime = datetime.datetime.now()

@Clinton.on_message(filters.command(["start"]))
async def start(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Scripted.START_TEXT.format(update.from_user.first_name),
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='📍 Cʜᴀɴɴᴇʟ 📍', url=f'https://t.me/{Config.UPDATE_CHANNEL}'),
                                                 InlineKeyboardButton(text='😒 Sᴏᴜʀᴄᴇ 😒', url='https://github.com/LISA-KOREA/Rename-bot') ],
                                               [ InlineKeyboardButton(text='🔐 Cʟᴏꜱᴇ 🔐', callback_data='cancel') ] ] ) )


@Clinton.on_message(filters.command(["help"]))
async def helpme(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Scripted.HELP_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='🔐 ᴄʟᴏꜱᴇ', callback_data='cancel') ] ] ) )



@Clinton.on_message(filters.command(["about"]))
async def abot(bot, update):
          await bot.send_message(
          chat_id=update.chat.id,
          text=Scripted.ABOUT_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text='🔐 ᴄʟᴏꜱᴇ', callback_data='cancel') ] ] ) )



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = Config.UPDATE_CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ!\n\nDᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs Cᴀɴ Usᴇ Mᴇ!",reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([ [ InlineKeyboardButton("🔰 Jᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ 🔰" ,url=f"https://t.me/{Config.UPDATE_CHANNEL}") ]   ]))
       		return
       date = message.date
       _used_date = find_one(user_id)
       used_date = _used_date["date"]      
       c_time = time.time()
       LIMIT = 240
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:
       	await app.send_chat_action(message.chat.id, "typing")
       	await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```",reply_to_message_id = message.message_id)
       else:
       	
       	media = await client.get_messages(message.chat.id,message.message_id)
       	file = media.document or media.video or media.audio 
       	dcid = FileId.decode(file.file_id).dc_id
       	filename = file.file_name
       	filesize = humanize.naturalsize(file.file_size)
       	fileid = file.file_id
       	await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid} """,reply_to_message_id = message.message_id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
