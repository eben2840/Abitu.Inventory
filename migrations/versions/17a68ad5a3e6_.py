"""empty message

Revision ID: 17a68ad5a3e6
Revises: e870cb2c9c06
Create Date: 2023-10-07 12:44:55.592624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17a68ad5a3e6'
down_revision = 'e870cb2c9c06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('qualities', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('reason', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('reason')
        batch_op.drop_column('qualities')

    # ### end Alembic commands ###