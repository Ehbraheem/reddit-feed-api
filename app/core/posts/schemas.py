from typing import Optional

from pydantic import BaseModel, AnyUrl, constr, root_validator


AUTHOR_REGEX = r"^(?=(t2_))\1[a-z0-9]{8}$"


class PostBase(BaseModel):
    title: str
    link: Optional[AnyUrl] = None
    author: constr(regex=AUTHOR_REGEX)
    subreddit: str
    content: Optional[str] = None
    promoted: bool = False
    nsfw: bool = False
    score: int = 0

    @root_validator()
    def valid_link_or_content(cls, values: dict) -> dict:
        provided_values = [values.get(k) for k in ["link", "content"] if values.get(k) is not None]
        if len(provided_values) > 1:
            raise ValueError("Provide either link or content, not both")
        elif not any(provided_values):
            raise ValueError("Provide either link or content")

        return values


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True
