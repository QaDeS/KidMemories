"""empty message

Revision ID: 7da3bd9e7004
Revises: 3e7b1f83f88b
Create Date: 2021-02-10 15:25:44.952796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7da3bd9e7004'
down_revision = '3e7b1f83f88b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('groupid', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_user_groupid'), 'user', ['groupid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_groupid'), table_name='user')
    op.drop_column('user', 'groupid')
    # ### end Alembic commands ###