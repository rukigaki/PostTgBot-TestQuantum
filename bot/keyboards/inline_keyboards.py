from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.handlers import MyCallback
import aiohttp


async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8000/posts") as response:
            posts = await response.json()
            inkb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=post["title"],
                                                                               callback_data=MyCallback(name_inb=post["title"],
                                                                                                        id_post=post["id"]).pack()) for post in posts]])
            return inkb
