from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine
from app.models import Base
from app.routes import router
from app.login import app_login



@asynccontextmanager
async def lifespan(application: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)
app.include_router(app_login)


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)