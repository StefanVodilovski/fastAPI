"""auto-votes table

Revision ID: d7b279e68844
Revises: d231b71a7352
Create Date: 2023-08-31 18:19:26.650323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'd7b279e68844'
down_revision: Union[str, None] = 'd231b71a7352'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('posts_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['posts_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('users_id', 'posts_id')
    )
    op.drop_column('posts', 'users_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
