from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import PostCreate, PostRead, PostUpdate
from app.crud import create_post, get_posts, get_post, update_post, delete_post



router = APIRouter()


@router.post("/posts", response_model=PostCreate)
async def endpoint_create_post(post: PostCreate, db: AsyncSession = Depends(get_db)):

    new_post = await create_post(db, post)

    return new_post


@router.get("/posts", response_model=list[PostRead])
async def endpoint_get_posts(db: AsyncSession = Depends(get_db)):
    posts = await get_posts(db)

    return posts

@router.get("/posts/{id_post}", response_model=PostRead)
async def endpoint_get_post(id_post: int, db: AsyncSession = Depends(get_db)):
    post = await get_post(id_post, db)

    return post


@router.put("/posts/{id_post}")
async def endpoint_update_post(id_post: int, data: PostUpdate, db: AsyncSession = Depends(get_db)):
    updated_post = await update_post(id_post, db, data.model_dump())

    return updated_post


@router.delete("/posts/{id_post}")
async def endpoint_delete_post(id_post: int, db: AsyncSession = Depends(get_db)):
    deleted_post = await delete_post(id_post, db)

    return deleted_post


