"""empty message

Revision ID: 954bcb85c25e
Revises: 2ea45c34ff72
Create Date: 2024-02-10 12:33:41.342789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '954bcb85c25e'
down_revision = '2ea45c34ff72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('waitlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('waitlist')
    # ### end Alembic commands ###