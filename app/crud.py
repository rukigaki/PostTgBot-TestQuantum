from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
from app.models import Post


#create

async def create_post(db: AsyncSession, post: schemas.PostCreate):
    new_post = models.Post(
        title=post.title,
        content=post.content,
    )

    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post


#read

async def get_posts(db: AsyncSession):
    result = await db.execute(select(Post))
    posts = result.scalars().all()
    return posts


async def get_post(id_post: int, db: AsyncSession):
    result = await db.execute(select(Post).where(Post.id == id_post))
    post = result.scalars().first()

    return post


#update

async def update_post(post_id: int, db: AsyncSession, new_data: dict):
    await db.execute(update(Post).where(Post.id == post_id).values(**new_data))
    await db.commit()
    result = await db.execute(select(Post).where(Post.id == post_id))
    result = result.scalars().first()

    return f"Вы успешно обновили данные {result}"

#delete

async def delete_post(post_id: int, db: AsyncSession):
    await db.execute(delete(Post).where(Post.id == post_id))
    await db.commit()

    return True
