"""Update metrics table to composite primary key

Revision ID: d7eadee9dda8
Revises: 60feb0050151
Create Date: 2025-07-27 04:52:30.845686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7eadee9dda8'
down_revision: Union[str, Sequence[str], None] = '60feb0050151'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop layouts table
    op.drop_table('layouts')
    # Change id column type if needed
    op.alter_column('metrics', 'id',
               existing_type=sa.UUID(),
               type_=sa.String(),
               existing_nullable=False)
    # Drop old primary key constraint
    op.drop_constraint('metrics_pkey', 'metrics', type_='primary')
    # Create new composite primary key
    op.create_primary_key('metrics_pkey', 'metrics', ['id', 'query_id'])


def downgrade() -> None:
    op.drop_constraint('metrics_pkey', 'metrics', type_='primary')
    op.create_primary_key('metrics_pkey', 'metrics', ['id'])
    op.alter_column('metrics', 'id',
               existing_type=sa.String(),
               type_=sa.UUID(),
               existing_nullable=False)
    # ...existing code for recreating layouts...
