from sqlalchemy.orm import Session
from sqlalchemy import func, text
from app.db.base import Post
from .schemas import PostCreate, Post as PostSchema

def get_posts(db: Session, skip: int = 0, limit: int = 27) -> list([PostSchema]):
    subquery = db.query(
        Post.id,
        Post.title,
        Post.author,
        Post.link,
        Post.subreddit,
        Post.content,
        Post.promoted,
        Post.nsfw,
        Post.score,
    ).order_by(
        Post.score.desc(),
        Post.nsfw.desc(),
        Post.promoted.asc(),
    ).subquery()

    return db.query(subquery).offset(skip).limit(limit).all()


def create_post(db: Session, post: PostCreate) -> PostSchema:
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post
