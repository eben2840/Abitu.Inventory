"""empty message

Revision ID: b96ebadc161b
Revises: c58b54494f23
Create Date: 2024-05-04 16:32:20.553600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b96ebadc161b'
down_revision = 'c58b54494f23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('manufacturing', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('coorperate', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('retail', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.drop_column('retail')
        batch_op.drop_column('coorperate')
        batch_op.drop_column('manufacturing')

    # ### end Alembic commands ###
