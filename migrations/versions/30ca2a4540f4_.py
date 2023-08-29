"""empty message

Revision ID: 30ca2a4540f4
Revises: a6804d733eee
Create Date: 2023-08-29 09:30:53.293333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30ca2a4540f4'
down_revision = 'a6804d733eee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leaders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('director', sa.String(), nullable=True),
    sa.Column('directress', sa.String(), nullable=True),
    sa.Column('others', sa.String(), nullable=True),
    sa.Column('ministries', sa.String(), nullable=True),
    sa.Column('total_number', sa.String(), nullable=True),
    sa.Column('timestamp', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('program', schema=None) as batch_op:
        batch_op.drop_column('total_number')
        batch_op.drop_column('others')
        batch_op.drop_column('ministries')
        batch_op.drop_column('director')
        batch_op.drop_column('timestamp')
        batch_op.drop_column('directress')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('program', schema=None) as batch_op:
        batch_op.add_column(sa.Column('directress', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('timestamp', sa.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('director', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('ministries', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('others', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('total_number', sa.VARCHAR(), nullable=True))

    op.drop_table('leaders')
    # ### end Alembic commands ###
