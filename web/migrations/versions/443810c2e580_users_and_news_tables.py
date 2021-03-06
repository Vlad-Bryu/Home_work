"""users and news tables

Revision ID: 443810c2e580
Revises: 
Create Date: 2019-06-14 18:25:01.324535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '443810c2e580'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=10), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
