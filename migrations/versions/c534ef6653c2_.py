"""empty message

Revision ID: c534ef6653c2
Revises: 63c74c30602a
Create Date: 2021-03-04 23:20:43.011121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c534ef6653c2'
down_revision = '63c74c30602a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('checked', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'checked')
    # ### end Alembic commands ###