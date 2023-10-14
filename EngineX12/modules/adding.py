# All Credit Goes To Ayush!
import time
import csv
import asyncio
from EngineX12 import app
from pyrogram import filters
from pyrogram.errors import FloodWait, UserAlreadyParticipant, UserPrivacyRestricted
from pyrogram.enums import UserStatus
from config import OWNER_ID
from EngineX12.modules.scrape import filenm


temploaded = []
from_file = []
freeze_time = 0


@app.on_message(filters.command("add") & filters.user(OWNER_ID))
async def adding(client, message):
	nrop = await message.reply_text("🔄 Loading Task...")
	if len(message.command) < 2:
		await nrop.edit_text("Adding Offline Members Becouse You Didn't Told me...")
	nropp = await nrop.edit_text(f"🤖 Scaning Members...")
	# Started Driver Code
	if len(temploaded)==0:
		await message.reply_text(f"<b>⚠️ WARNING:</b>\nYou Didn't scrapped members from your members target group! next time, scrape members via /scrape <Group Username/ID>\n\nSearching For backup log...")
		try:
			file = open(f'{filenm}.csv','r')
			a = file.readlines()
			b = " ".join(a)
			c = b.split()
			for i in c:
				if i.isdigit():
					from_file.append(int(i))
			await nropp.edit_text(f"{len(from_file)} Members Loaded From Your Scraped File ❇️!\nNow Starting Adding Members...")
		except FileNotFoundError:
			await nrop.edit_text(f"♻️ You Have No File Of Own Scrapped Group!\n\nTrying To Add from Ayush's File!")
			file = open(f'premium.csv','r')
			a = file.readlines()
			b = " ".join(a)
			c = b.split()
			for i in c:
				if i.isdigit():
					from_file.append(int(i))
			await message.reply_text(f"{from_file} Members Loaded From Ayush's File ✅!\n\n(Not Recommended Everytime Using My File!)")
	# End Of Driver Code
	if len(from_file) < 50:
		print(from_file)
	if len(temploaded) > 0:
		domtor = temploaded
	else:
		domtor = from_file
	finallyw = await message.reply_text(f"{len(domtor)} Members Loaded! ✅\nNow Adding Members According To Your Choice...")

	addedd = 0
	cancledd = 0
	privacyy = 0
	alreaddy = 0
	if "online" in message.text:
		member_type = ["userstatus.recently", "userstatus.online"]
	else:
		member_type = ["userstatus.long_ago", "userstatus.last_month", "userstatus.last_week"]
	try:
		for membar in domtor:
			try:
				user = await app.get_users(membar)
				if (str(user.status)).lower() in member_type:
					try:
						await app.add_chat_members(message.chat.id, user.id)
						addedd += 1
						print("Member Added!-----------✅")
						if freeze_time > 1:
							time.sleep(freeze_time)
					except UserAlreadyParticipant:
						alreaddy += 1
					except UserPrivacyRestricted:
						privacyy += 1
					except FloodWait as e:
						await message.reply_text(f"Telegram Gave You Flood Of {e.value} seconds! Paused for {e.value} seconds!")
						await asyncio.sleep(int(e.value))
					except:
						cancledd += 1
			except FloodWait as lol:
				print(f"WARNING :- \n\nFLOOD WAIT FOR {lol.value}]\n\nTelegram Give You FloodWait! It's not script's issue, It's Telegram Issue!")
				await asyncio.sleep(int(lol.value))
		await message.reply_text(f"<b>TASK COMPLETED! ✅</b>\n<code>---------------</code>\n<b>REPORT</b>:\n<b>Members Loaded</b> : <code>{len(domtor)}</code>\n<b>Added</b> : <code>{addedd}</code>\n<b>Cancelled By Privacy</b> : <code>{privacyy}</code>\n<b>Skipped</b> : <code>{cancledd}</code>\n<b>Already Members</b> : <code>{alreaddy}</code>")
	except:
		await message.reply_text(f"<b>TASK FAILED! ⚠️</b>\n<code>---------------</code>\n<b>REPORT</b>:\n<b>Members Loaded</b> : <code>{len(domtor)}</code>\n<b>Added</b> : <code>{addedd}</code>\n<b>Cancelled By Privacy</b> : <code>{privacyy}</code>\n<b>Skipped</b> : <code>{cancledd}</code>\n<b>Already Members</b> : <code>{alreaddy}</code>\n\nPlease Clone Repo again or check your telegram account!")


@app.on_message(filters.command("delay") & filters.user(OWNER_ID))
async def settimer(client, message):
	global freeze_time
	try:
		timee = message.text.split(" ", maxsplit=1)[1]
	except IndexError:
		return await message.reply_text("Error BSDK!")
	if timee.isdigit:
		freeze_time += timee
		await message.reply_text(f"Your Script Have Been Set To {freeze_time}! ✅\n\nScript will stop after every member added. It's Normal!!")
	else:
		await message.reply_text(f"GIVE FREEZE TIME IN SECONDS! Ex. /delay 5")


@app.on_message(filters.command("load") & filters.user(OWNER_ID))
async def loads(client, message):
	if len(message.command) < 2:
		return await message.reply_text("**Please Give Group's Username!**")
	try:
		group_username = message.text.split(" ", maxsplit=1)[1]
	except IndexError:
		return await message.delete()
	replyreport = await message.reply_text(f"🔄**Members loading from {group_username}...**")
	try:
		async for member in app.get_chat_members(group_username):
			temploaded.append(member.user.id)
		replreport = await message.reply_text(f"🔄<b>{len(temploaded)} Members loaded from {group_username}!</b>")
	except Exception as exc:
		eplyreport = await message.reply_text(f"<b>ERROR</b>:\n\n{exc}")


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#                             - Property of Ayush -                               #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
