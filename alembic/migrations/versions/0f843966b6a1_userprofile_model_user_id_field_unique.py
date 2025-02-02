"""userprofile model user_id field unique

Revision ID: 0f843966b6a1
Revises: 7ba4c753990d
Create Date: 2025-01-30 17:26:56.106982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f843966b6a1'
down_revision: Union[str, None] = '7ba4c753990d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user_profiles', ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_profiles', type_='unique')
    # ### end Alembic commands ###
