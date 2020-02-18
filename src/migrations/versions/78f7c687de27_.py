"""empty message

Revision ID: 78f7c687de27
Revises: 0c79a7518a3c
Create Date: 2020-02-18 16:05:13.972155

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '78f7c687de27'
down_revision = '0c79a7518a3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('avg_rating', sa.String(length=128), nullable=True))
    op.add_column('game', sa.Column('link', sa.String(length=128), nullable=True))
    op.add_column('game', sa.Column('num_voters', sa.String(length=128), nullable=True))
    op.add_column('game', sa.Column('rank_bgg', sa.String(length=10), nullable=True))
    op.alter_column('game', 'bgg_rate',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('game', 'player_max',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('game', 'player_min',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('game', 'player_rate',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('game', 'player_rate',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('game', 'player_min',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('game', 'player_max',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('game', 'bgg_rate',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.drop_column('game', 'rank_bgg')
    op.drop_column('game', 'num_voters')
    op.drop_column('game', 'link')
    op.drop_column('game', 'avg_rating')
    # ### end Alembic commands ###