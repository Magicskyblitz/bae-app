"""Changed table format

Revision ID: 20ae64c95fbb
Revises: 
Create Date: 2023-11-14 19:18:29.790129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20ae64c95fbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('account_type', sa.String(length=20), nullable=False))
        batch_op.drop_column('username')
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=120), nullable=False))
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=20), nullable=False))
        batch_op.drop_column('account_type')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
