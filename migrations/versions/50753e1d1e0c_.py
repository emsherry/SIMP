"""empty message

Revision ID: 50753e1d1e0c
Revises: 
Create Date: 2023-05-05 06:47:35.810719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50753e1d1e0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth',
    sa.Column('email_id', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email_id'),
    sa.UniqueConstraint('password')
    )
    op.create_table('user_info',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('Email', sa.String(length=120), nullable=False),
    sa.Column('dob', sa.DateTime(), nullable=True),
    sa.Column('res_address', sa.String(length=120), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['auth.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('wallet',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('wallet_id', sa.Integer(), nullable=False),
    sa.Column('curr_bal', sa.Integer(), nullable=False),
    sa.Column('is_locked', sa.Boolean(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['auth.user_id'], ),
    sa.PrimaryKeyConstraint('wallet_id')
    )
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='test_pkey')
    )
    op.drop_table('wallet')
    op.drop_table('user_info')
    op.drop_table('auth')
    # ### end Alembic commands ###
