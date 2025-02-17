"""deleted_by deleted_at col added

Revision ID: 0116f0a8450b
Revises: 9690b3ad2e6c
Create Date: 2025-02-17 21:58:19.779960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0116f0a8450b'
down_revision: Union[str, None] = '9690b3ad2e6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('deleted_by_id', sa.CHAR(length=36), nullable=True))
    op.create_foreign_key(None, 'user', 'user', ['deleted_by_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'deleted_by_id')
    op.drop_column('user', 'deleted_at')
    # ### end Alembic commands ###
