import aiohttp
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix="post"):
    name_inb: str
    id_post: int


callback_router = Router()


@callback_router.callback_query(MyCallback.filter())
async def callback_post(callback: CallbackQuery, callback_data: MyCallback):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:8000/posts/{callback_data.id_post}") as response:
            posts = await response.json()
            await callback.answer()

            text_html = f"""<b>{posts["title"]}</b>\n
{posts["content"]}

<i>{posts["created_at"]}</i>"""

            await callback.message.answer(text=text_html, parse_mode="HTML")
