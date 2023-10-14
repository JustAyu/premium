import asyncio
import importlib

from pyrogram import idle
from EngineX12 import app
import config
from EngineX12.modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def initiate_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("EngineX12.modules." + all_module)
    print("Script Started!")
    await idle()
    print("Script Stopped!")


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
