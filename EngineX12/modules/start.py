import time
import random

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified

from EngineX12 import app
from config import OWNER_ID

helpline = """<b> All Commands - </b>
<code>---------------</code>
<code>---------------</code>


/scrape - Load members into CSV.
/add - /add offline/online.

/load - load members for a short period.
/stop - Stop adding members.

/help - To list all commands.
/info - Try this command before you use script.

CREDIT GOES TO > Ayush (Owner Of @Life_Codes)
#NoCopyPaste
"""

infoDOM = """
<b>INFORMATION ABOUT SCRIPT AND DEV!</b>
<code>------------------------------</code>

Hi, This Script was made by Ayush A to Z! As you already seen that This script doesn't require session string. It's becouse session string can be used as userbot but not good for adding members due to high sensitive! So for your account safety, I made this script as normal logging!

Soon I'll upgrade this script for supporting multiple account support after good performance!

PLEASE NOTE :
I made this script, I TRIED THIS SCRIPT ON MY 3 ACCOUNTS! It's working fine and didn't harmed my accounts!........BUT I'M NOT <b>responsible</b> If your account get banned or deleted! I'll just lough on you, SO USE ON YOUR RISK!

TIPS :
Add offline members in your members for growing your group

NOTICE:
Give star and credits to Ayush for making this usefull script free for everyone and support me by joining your accounts in my channel @Life_codes

Thank You!
"""

@app.on_message(filters.command(["help"]) & filters.user(OWNER_ID))
async def on_help(_, message: Message):
    await message.reply_text(helpline)

@app.on_message(filters.command(["info"]) & filters.user(OWNER_ID))
async def on_help(_, message: Message):
    await message.reply_text(infoDOM)