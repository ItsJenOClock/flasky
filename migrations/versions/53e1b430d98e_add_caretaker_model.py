"""add Caretaker model

Revision ID: 53e1b430d98e
Revises: 62cf37951ee8
Create Date: 2024-11-06 05:13:19.796715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53e1b430d98e'
down_revision = '62cf37951ee8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caretaker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('caretaker')
    # ### end Alembic commands ###
