"""set default_ttl

Revision ID: 49e21e1bb766
Revises: 91cc2dd4ae43
Create Date: 2021-12-06 12:52:22.527979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49e21e1bb766'
down_revision = '91cc2dd4ae43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(f"UPDATE switches SET ttl=14")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(f"UPDATE switches SET ttl=60")
    # ### end Alembic commands ###