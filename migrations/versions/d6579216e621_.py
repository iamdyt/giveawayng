"""empty message

Revision ID: d6579216e621
Revises: 
Create Date: 2020-06-21 06:50:59.712511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6579216e621'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('benefits', sa.Column('thumbone', sa.String(length=50), nullable=False))
    op.add_column('benefits', sa.Column('thumbthree', sa.String(length=50), nullable=False))
    op.add_column('benefits', sa.Column('thumbtwo', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('benefits', 'thumbtwo')
    op.drop_column('benefits', 'thumbthree')
    op.drop_column('benefits', 'thumbone')
    # ### end Alembic commands ###
