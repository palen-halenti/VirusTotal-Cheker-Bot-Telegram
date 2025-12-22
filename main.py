import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from assets.config import TOKEN
from assets.commands import route as commands_router

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
          )
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(commands_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
