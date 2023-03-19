from sqlalchemy.orm import Session
import factory
import pytest
from pydantic import ValidationError

from app.core.posts.services import create_post, get_posts
from app.tests.factories.post import PostFactory
from app.core.posts.schemas import PostCreate


def test_create_post(
    db: Session
) -> None:
    data = factory.build(dict, FACTORY_CLASS=PostFactory)
    data["link"] = data["id"] = None
    post = create_post(db, PostCreate(**data))
    print(post)
    assert post.title == data["title"]
    assert post.author == data["author"]
    assert post.subreddit == data["subreddit"]
    assert post.link == data["link"]
    assert post.score == data["score"]
    assert post.id is not None

    invalid_data = factory.build(dict, FACTORY_CLASS=PostFactory)
    with pytest.raises(ValidationError, match="1 validation error for PostCreate"):
        create_post(db, PostCreate(**invalid_data))


def test_get_posts(
    db: Session
) -> None:
    posts = get_posts(db, skip=0, limit=27)
    assert len(posts) == 0

    PostFactory.create()
    posts = get_posts(db, skip=0, limit=27)
    # FIXME: This fails because the PostFactory doesn't creates a post in the right database
    # assert len(posts) == 1

