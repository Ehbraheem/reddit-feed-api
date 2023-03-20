from factory import Factory, Sequence, Faker
from core.posts.models import Post

class PostFactory(Factory):
    class Meta:
        model = Post

    id = Sequence(lambda n: n)
    title = Faker('sentence')
    author = 't2_11qnzrqv'
    link = Faker('url')
    subreddit = Faker('word')
    content = Faker('paragraph')
    promoted = Faker('boolean')
    nsfw = Faker('boolean')
    score = Faker('pyint')
