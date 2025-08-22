"""update training pair hashtag table

Revision ID: 31f1b209458b
Revises: e27de6cdf9d4
Create Date: 2025-08-04 11:13:55.922990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31f1b209458b'
down_revision: Union[str, None] = 'e27de6cdf9d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    -- Drop the composite primary key constraint first
    ALTER TABLE training_pair_hashtags 
    DROP CONSTRAINT IF EXISTS training_pair_hashtags_pkey;
    
    -- Drop the hashtag_id column
    ALTER TABLE training_pair_hashtags
    DROP COLUMN IF EXISTS hashtag_id;

    -- Add id column as primary key
    ALTER TABLE training_pair_hashtags
    ADD COLUMN id UUID PRIMARY KEY DEFAULT uuid_generate_v4();

    -- Add hashtag column
    ALTER TABLE training_pair_hashtags
    ADD COLUMN hashtag VARCHAR(255) NOT NULL;
    ''')


def downgrade() -> None:
    op.execute('''
    -- Drop the hashtag column
    ALTER TABLE training_pair_hashtags
    DROP COLUMN IF EXISTS hashtag;
    
    -- Drop the id column
    ALTER TABLE training_pair_hashtags
    DROP COLUMN IF EXISTS id;
    
    -- Add back hashtag_id column
    ALTER TABLE training_pair_hashtags
    ADD COLUMN hashtag_id UUID REFERENCES hashtags(id) ON DELETE CASCADE;
    
    -- Recreate the composite primary key
    ALTER TABLE training_pair_hashtags
    ADD PRIMARY KEY (training_pair_id, hashtag_id);
    ''')
