import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from NoinoiMusic.utils.filters import command

from NoinoiMusic import BOT_NAME, BOT_USERNAME
from NoinoiMusic.config import BOT_USERNAME 
from NoinoiMusic.config import BOT_NAME
from NoinoiMusic.config import START_IMG

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**Welcome {message.from_user.mention()}** ๐

This is the **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Bot,** a bot for playing high quality and unbreakable music in your groups voice chat.

Just add me to your group & make as a admin with needed admin permissions to perform a right actions, now let's enjoy your music!

Use the given buttons for more info๐""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐Commands ๐", callback_data="cbcmnds"),
                    InlineKeyboardButton(
                        "๐ค About ๐ค", callback_data="cbabout")
                ],
                [
                    InlineKeyboardButton(
                        "โฅ๏ธ Basic Guide โฅ๏ธ", callback_data="cbguide")
                ],
                [
                    InlineKeyboardButton(
                        "๐ Add Bot in Your Group ๐", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        ),
    )
