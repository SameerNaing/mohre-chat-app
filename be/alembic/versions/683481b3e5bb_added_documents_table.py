"""Added documents table

Revision ID: 683481b3e5bb
Revises: 
Create Date: 2025-01-21 10:31:34.188417

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '683481b3e5bb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.CHAR(length=36), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('hash', sa.String(length=255), nullable=False),
    sa.Column('source', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('document')
    # ### end Alembic commands ###
