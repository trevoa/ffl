"""empty message

Revision ID: 6dbb8fb1c3ab
Revises: 1159a970b737
Create Date: 2018-10-01 21:35:00.115765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dbb8fb1c3ab'
down_revision = '1159a970b737'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nfl_boxscore_game', sa.Column('week', sa.String(length=32), nullable=True))
    op.add_column('nfl_boxscore_game', sa.Column('year', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('nfl_boxscore_game', 'year')
    op.drop_column('nfl_boxscore_game', 'week')
    # ### end Alembic commands ###