"""empty message

Revision ID: 047a68039153
Revises: 1c2ccde08f66
Create Date: 2024-12-22 09:10:38.803273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '047a68039153'
down_revision = '1c2ccde08f66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###