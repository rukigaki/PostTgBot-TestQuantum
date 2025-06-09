from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.keyboards import fetch_posts


telegram_router = Router()


@telegram_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text="Добро пожаловать!")


@telegram_router.message(Command("posts"))
async def post_handler(message: Message):
    await message.answer(text="Вот ваши посты!", reply_markup=await fetch_posts())
