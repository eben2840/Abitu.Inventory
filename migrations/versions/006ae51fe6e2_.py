"""empty message

Revision ID: 006ae51fe6e2
Revises: d25e683a4e03
Create Date: 2024-04-19 17:54:39.145099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '006ae51fe6e2'
down_revision = 'd25e683a4e03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.alter_column('clientid',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.alter_column('clientid',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
