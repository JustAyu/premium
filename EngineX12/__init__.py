import config
import asyncio
from pyrogram import Client


loop = asyncio.get_event_loop()

app = Client(name="ayush", api_id=config.API_ID, api_hash=config.API_HASH)

async def initiate_bot():
    await app.start()

loop.run_until_complete(initiate_bot())