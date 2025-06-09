import asyncio
from app.main import app as fastapi_app
import uvicorn


from bot.bot import start_bot

async def main():
    api_task = asyncio.create_task(
        asyncio.to_thread(uvicorn.run, fastapi_app, host="127.0.0.1", port=8000)
    )

    bot_task = asyncio.create_task(start_bot())

    await asyncio.gather(api_task, bot_task)

if __name__ == "__main__":
    asyncio.run(main())