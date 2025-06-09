from aiogram import Bot, Dispatcher
import asyncio
from bot.handlers import telegram_router, callback_router
from config import settings


bot = Bot(settings.api_token_bot)
dispatcher = Dispatcher()
dispatcher.include_routers(callback_router, telegram_router)


async def start_bot():
    await dispatcher.start_polling(bot)


# if __name__ == "__main__":
#     asyncio.run(main())