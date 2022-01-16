import os
from pyrogram import Client, filters
from pyrogram.types import *

from MashaRoBot.conf import get_str_key
from MashaRoBot import pbot
 
 # pls don't delete
REPO_TEXT = "**PHOENIX [BOT](https://telegra.ph/file/6502c7fa93135c478e5a2.jpg) will Make Your Groups Secured And it's have a lot of fun features (:  ! \n\n↼ Owner ⇀ : 『 [Telegram pro](t.me/TheTelegrampro) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @THANIMAIBOTS «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("💥ADD YOUR GROUP💥", url=f"https://github.com/proTamizhan/thanimaibot"),
        InlineKeyboardButton("💥STATUS💥", url=f"https://t.me/phoenixcreatio"),
      ],[
        InlineKeyboardButton("ᴏᴡɴᴇʀ 😈", url="https://t.me/Jaihindupuramking"),
        InlineKeyboardButton("💥ꜱᴜᴘᴘᴏʀᴛ💥", url="https://t.me/phoenixbotspport"),
       InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Jaihindupuramking"),
      ],[
        InlineKeyboardButton("💥ᴜᴘᴅᴀᴛᴇꜱ💥", url="https://t.me/phoenixrules1"),
        InlineKeyboardButton("😈ᴅᴇᴠᴇʟᴏᴘᴇʀ😈", url="https://t.me/jaihindupuram_king"),
       InlineKeyboardButton("💥GROUP 💥", url="https://t.me/PHOENIX_CHAT_TAMIL"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
