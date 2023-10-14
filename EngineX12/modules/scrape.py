# All Credit Goes To Ayush!
import asyncio
from EngineX12 import app
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.enums import UserStatus
from config import OWNER_ID
import csv

filenm = "Scraped"
members = []

@app.on_message(filters.command("scrape") & filters.user(OWNER_ID))
async def scrapingg(client, message):
	nrop = await message.reply_text(f"🔄 Scraping members into <b>{filenm}.txt</b>...")
	if len(message.command) < 2:
		return await nrop.edit_text("Please Give A Public Group's Username in this style <code>/scrape cornography</code>\n\nMake Sure Targeted Group Members Are Not Hidden!")
	try:
		group_username = message.text.split(" ", maxsplit=1)[1]
	except IndexError:
		return await nrop.edit_text("IndexError Occured!\nTry with other group's username!")
	await nrop.edit_text(f"<b>🔄 ••• SCRAPING ••• 🔄")
	try:
		async for member in app.get_chat_members(group_username):
			members.append(member.user.id)
		await nrop.edit_text(f"<b>✅ •• PACKING •• ✅")
		file = open(f'{filenm}.csv','w')
		for dongrila in members:
			file.write(f"{str(dongrila)} ")
		file.close()
		return await nrop.edit_text(f"<b>✅ • SCRAPED • ✅")

	except Exception as exc:
		await nrop.edit_text(f"<b>❌ • ERROR • ❌\n\n<code>{exc}</code>")


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#                    - Property of Ayush -                                        #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#