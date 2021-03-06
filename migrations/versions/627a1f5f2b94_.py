"""empty message

Revision ID: 627a1f5f2b94
Revises: 
Create Date: 2019-05-07 10:09:22.556413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '627a1f5f2b94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('excerpt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('score',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wpm', sa.Integer(), nullable=False),
    sa.Column('excerpt_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excerpt_id'], ['excerpt.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('score')
    op.drop_table('excerpt')
    # ### end Alembic commands ###
