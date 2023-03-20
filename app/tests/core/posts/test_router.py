from fastapi.testclient import TestClient
from app.tests.factories.post import PostFactory
from sqlalchemy.orm import Session

def test_create_new_post(
    client: TestClient, db: Session
) -> None:
    data = { "title": "Foo", "author": "t2_11qnzrqv", "subreddit": "r/learnpython", "link": "https://www.reddit.com/r/learnpython/comments/9x0q0p/what_is_the_best_way_to_learn_python/", "score": 1 }
    response = client.post(
        "posts/", json=data,
    )

    assert response.status_code == 200
    content = response.json()
    validate_post(content)
    assert content["title"] == data["title"]
    assert content["author"] == data["author"]
    assert content["subreddit"] == data["subreddit"]
    assert content["link"] == data["link"]
    assert content["score"] == data["score"]
    assert "id" in content

def test_read_posts(
    client: TestClient, db: Session
) -> None:
    PostFactory.create_batch(10)
    response = client.get("posts/")
    print(len(response.json()))
    assert response.status_code == 200
    content = response.json()
    assert len(content) > 0
    map(validate_post, content)


def validate_post(post: dict) -> None:
    assert "title" in post
    assert "author" in post
    assert "subreddit" in post
    assert "link" in post
    assert "score" in post
    assert "id" in post
