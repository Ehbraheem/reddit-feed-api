from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app.dependencies import get_db
from .services import get_posts, create_post
from .schemas import Post, PostCreate

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 27, db: Session = Depends(get_db)):
    posts = get_posts(db, skip=skip, limit=limit)
    return posts


@router.post("/", response_model=Post)
def create_new_post(post: PostCreate, db: Session = Depends(get_db)) -> Post:
    return create_post(db=db, post=post)
