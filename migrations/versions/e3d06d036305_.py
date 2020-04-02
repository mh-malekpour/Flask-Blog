"""empty message

Revision ID: e3d06d036305
Revises: 5b0cec2f60f8
Create Date: 2020-04-02 18:17:14.142191

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e3d06d036305'
down_revision = '5b0cec2f60f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('summary', sa.String(length=256), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('slug', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug'),
    sa.UniqueConstraint('title')
    )
    op.drop_index('slug', table_name='post')
    op.drop_index('title', table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('summary', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('slug', mysql.VARCHAR(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('title', 'post', ['title'], unique=True)
    op.create_index('slug', 'post', ['slug'], unique=True)
    op.drop_table('posts')
    # ### end Alembic commands ###
