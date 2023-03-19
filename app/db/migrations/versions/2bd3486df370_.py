"""empty message

Revision ID: 2bd3486df370
Revises: 
Create Date: 2023-03-16 17:22:32.704492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bd3486df370'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('subreddit', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('promoted', sa.Boolean(), nullable=True),
    sa.Column('nsfw', sa.Boolean(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_author'), 'posts', ['author'], unique=False)
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    op.create_index(op.f('ix_posts_nsfw'), 'posts', ['nsfw'], unique=False)
    op.create_index(op.f('ix_posts_promoted'), 'posts', ['promoted'], unique=False)
    op.create_index(op.f('ix_posts_score'), 'posts', ['score'], unique=False)
    op.create_index(op.f('ix_posts_subreddit'), 'posts', ['subreddit'], unique=False)
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_index(op.f('ix_posts_subreddit'), table_name='posts')
    op.drop_index(op.f('ix_posts_score'), table_name='posts')
    op.drop_index(op.f('ix_posts_promoted'), table_name='posts')
    op.drop_index(op.f('ix_posts_nsfw'), table_name='posts')
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_index(op.f('ix_posts_author'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###
