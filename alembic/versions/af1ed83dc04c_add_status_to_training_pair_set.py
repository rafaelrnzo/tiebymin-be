"""add status to training pair set

Revision ID: af1ed83dc04c
Revises: e8365edf484e
Create Date: 2025-08-04 23:00:47.119650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af1ed83dc04c'
down_revision: Union[str, None] = 'e8365edf484e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add review status fields to training_pair_sets table
    op.add_column('training_pair_sets', sa.Column('review_status', sa.String(50), nullable=True, default='QUEUE'))
    op.add_column('training_pair_sets', sa.Column('reviewed_at', sa.DateTime(), nullable=True))
    op.add_column('training_pair_sets', sa.Column('reviewed_by', sa.String(100), nullable=True))
    
    # Create index for better query performance
    op.create_index(op.f('ix_training_pair_sets_review_status'), 'training_pair_sets', ['review_status'], unique=False)


def downgrade():
    # Remove the added columns
    op.drop_index(op.f('ix_training_pair_sets_review_status'), table_name='training_pair_sets')
    op.drop_column('training_pair_sets', 'reviewed_by')
    op.drop_column('training_pair_sets', 'reviewed_at')
    op.drop_column('training_pair_sets', 'review_status') 