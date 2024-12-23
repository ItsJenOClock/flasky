"""empty message

Revision ID: f466f88866f3
Revises: 5f6bb947ff0b
Create Date: 2024-12-23 03:34:30.296820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f466f88866f3'
down_revision = '5f6bb947ff0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caretaker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cat',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.Column('personality', sa.String(), nullable=False),
    sa.Column('pet_count', sa.Integer(), nullable=True),
    sa.Column('caretaker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['caretaker_id'], ['caretaker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cat')
    op.drop_table('caretaker')
    # ### end Alembic commands ###