from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    link = Column(String, index=False)
    subreddit = Column(String, index=True)
    content = Column(String, index=False)
    promoted = Column(Boolean, index=True)
    nsfw = Column(Boolean, index=True)
    score = Column(Integer, index=True)

    def __repr__(self):
        return f"Feed(id={self.id}, title={self.title}, author={self.author}, link={self.link}, subreddit={self.subreddit}, content={self.content}, promoted={self.promoted}, nsfw={self.nsfw}, score={self.score})"
