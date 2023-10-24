"""empty message

Revision ID: 059d90ed6ff5
Revises: 89418ec29ddd
Create Date: 2023-10-24 14:04:40.338213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '059d90ed6ff5'
down_revision = '89418ec29ddd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('getfunds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('ministry', sa.String(), nullable=True),
    sa.Column('program', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('telephone', sa.String(), nullable=True),
    sa.Column('campus', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('getfunds')
    # ### end Alembic commands ###