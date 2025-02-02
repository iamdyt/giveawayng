"""empty message

Revision ID: f4dff0ca0396
Revises: 7f3859880aa7
Create Date: 2020-06-25 03:49:44.956049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4dff0ca0396'
down_revision = '7f3859880aa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('email', sa.String(length=25), nullable=False))
    op.add_column('admin', sa.Column('phone', sa.String(length=11), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admin', 'phone')
    op.drop_column('admin', 'email')
    # ### end Alembic commands ###
