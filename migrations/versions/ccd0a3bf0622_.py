"""empty message

Revision ID: ccd0a3bf0622
Revises: 8c0320e3730e
Create Date: 2018-10-21 17:53:46.587244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd0a3bf0622'
down_revision = '8c0320e3730e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'nfl_game', ['detail_id'])
    op.create_table('nfl_live_player_game_stats',
    sa.Column('game_detail_id', sa.String(length=64), nullable=False),
    sa.Column('team_abbr', sa.String(length=32), nullable=True),
    sa.Column('person_name', sa.String(length=128), nullable=True),
    sa.Column('person_id', sa.String(length=64), nullable=False),
    sa.Column('defensive_assists', sa.Float(), nullable=True),
    sa.Column('defensive_interceptions', sa.Float(), nullable=True),
    sa.Column('defensive_interceptions_yards', sa.Float(), nullable=True),
    sa.Column('defensive_forced_fumble', sa.Float(), nullable=True),
    sa.Column('defensive_passes_defensed', sa.Float(), nullable=True),
    sa.Column('defensive_sacks', sa.Float(), nullable=True),
    sa.Column('defensive_safeties', sa.Float(), nullable=True),
    sa.Column('defensive_solo_tackles', sa.Float(), nullable=True),
    sa.Column('defensive_total_tackles', sa.Float(), nullable=True),
    sa.Column('defensive_tackles_for_a_loss', sa.Float(), nullable=True),
    sa.Column('touchdowns_defense', sa.Float(), nullable=True),
    sa.Column('fumbles_lost', sa.Float(), nullable=True),
    sa.Column('fumbles_total', sa.Float(), nullable=True),
    sa.Column('kick_returns', sa.Float(), nullable=True),
    sa.Column('kick_returns_long', sa.Float(), nullable=True),
    sa.Column('kick_returns_touchdowns', sa.Float(), nullable=True),
    sa.Column('kick_returns_yards', sa.Float(), nullable=True),
    sa.Column('kicking_fg_att', sa.Float(), nullable=True),
    sa.Column('kicking_fg_long', sa.Float(), nullable=True),
    sa.Column('kicking_fg_made', sa.Float(), nullable=True),
    sa.Column('kicking_xk_att', sa.Float(), nullable=True),
    sa.Column('kicking_xk_made', sa.Float(), nullable=True),
    sa.Column('passing_attempts', sa.Float(), nullable=True),
    sa.Column('passing_completions', sa.Float(), nullable=True),
    sa.Column('passing_touchdowns', sa.Float(), nullable=True),
    sa.Column('passing_yards', sa.Float(), nullable=True),
    sa.Column('passing_interceptions', sa.Float(), nullable=True),
    sa.Column('punt_returns', sa.Float(), nullable=True),
    sa.Column('punting_average_yards', sa.Float(), nullable=True),
    sa.Column('punting_long', sa.Float(), nullable=True),
    sa.Column('punting_punts', sa.Float(), nullable=True),
    sa.Column('punting_punts_inside20', sa.Float(), nullable=True),
    sa.Column('receiving_receptions', sa.Float(), nullable=True),
    sa.Column('receiving_target', sa.Float(), nullable=True),
    sa.Column('receiving_touchdowns', sa.Float(), nullable=True),
    sa.Column('receiving_yards', sa.Float(), nullable=True),
    sa.Column('rushing_attempts', sa.Float(), nullable=True),
    sa.Column('rushing_average_yards', sa.Float(), nullable=True),
    sa.Column('rushing_touchdowns', sa.Float(), nullable=True),
    sa.Column('rushing_yards', sa.Float(), nullable=True),
    sa.Column('kickoff_returns_touchdowns', sa.Float(), nullable=True),
    sa.Column('kickoff_returns_yards', sa.Float(), nullable=True),
    sa.Column('punt_returns_long', sa.Float(), nullable=True),
    sa.Column('opponent_fumble_recovery', sa.Float(), nullable=True),
    sa.Column('total_points_scored', sa.Float(), nullable=True),
    sa.Column('kick_returns_average_yards', sa.Float(), nullable=True),
    sa.Column('punt_returns_average_yards', sa.Float(), nullable=True),
    sa.Column('punt_returns_touchdowns', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['game_detail_id'], ['nfl_game.detail_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('game_detail_id', 'person_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'nfl_game', type_='unique')
    op.drop_table('nfl_live_player_game_stats')
    # ### end Alembic commands ###
