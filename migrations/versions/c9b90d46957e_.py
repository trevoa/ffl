"""empty message

Revision ID: c9b90d46957e
Revises: 
Create Date: 2017-08-08 09:05:16.016517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9b90d46957e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nfl_team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('espn_code', sa.String(length=32), nullable=True),
    sa.Column('espn_id', sa.Integer(), nullable=True),
    sa.Column('bye_week', sa.Integer(), nullable=True),
    sa.Column('projected_defense_points', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('espn_code', sa.String(length=8), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_email',
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_table('nfl_game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('home_team_id', sa.Integer(), nullable=True),
    sa.Column('away_team_id', sa.Integer(), nullable=True),
    sa.Column('season_week', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['away_team_id'], ['nfl_team.id'], ),
    sa.ForeignKeyConstraint(['home_team_id'], ['nfl_team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nfl_player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('espn_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('projected_points', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['nfl_team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nfl_player_position',
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('posiiton_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['nfl_player.id'], ),
    sa.ForeignKeyConstraint(['posiiton_id'], ['position.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nfl_player_position')
    op.drop_table('nfl_player')
    op.drop_table('nfl_game')
    op.drop_table('user_email')
    op.drop_table('position')
    op.drop_table('nfl_team')
    # ### end Alembic commands ###