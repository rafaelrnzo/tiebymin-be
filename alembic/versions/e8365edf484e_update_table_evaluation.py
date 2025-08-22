"""update table evaluation

Revision ID: e8365edf484e
Revises: 31f1b209458b
Create Date: 2025-08-04 21:53:53.958507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8365edf484e'
down_revision: Union[str, None] = '31f1b209458b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop foreign key constraints first
    op.execute('''
    -- Drop foreign key constraints
    ALTER TABLE IF EXISTS generated_training_pairs DROP CONSTRAINT IF EXISTS generated_training_pairs_ai_model_id_fkey;
    ALTER TABLE IF EXISTS generated_training_pairs DROP CONSTRAINT IF EXISTS generated_training_pairs_training_pair_id_fkey;
    ALTER TABLE IF EXISTS generated_hook_variants DROP CONSTRAINT IF EXISTS generated_hook_variants_training_pair_id_fkey;
    ALTER TABLE IF EXISTS generated_scenes DROP CONSTRAINT IF EXISTS generated_scenes_training_pair_id_fkey;
    ALTER TABLE IF EXISTS user_preferences DROP CONSTRAINT IF EXISTS user_preferences_user_id_fkey;
    ALTER TABLE IF EXISTS user_preferences DROP CONSTRAINT IF EXISTS user_preferences_training_pair_id_fkey;
    ALTER TABLE IF EXISTS user_preferences DROP CONSTRAINT IF EXISTS user_preferences_training_pair_set_id_fkey;
    ''')

    # Drop tables in correct order (child tables first, then parent tables)
    op.execute('''
    DROP TABLE IF EXISTS user_preferences CASCADE;
    DROP TABLE IF EXISTS generated_hook_variants CASCADE;
    DROP TABLE IF EXISTS generated_scenes CASCADE;
    DROP TABLE IF EXISTS generated_training_pairs CASCADE;
    DROP TABLE IF EXISTS training_pair_sets CASCADE;
    DROP TABLE IF EXISTS fine_tune_models CASCADE;
    DROP TABLE IF EXISTS ai_models CASCADE;
    ''')

    # Create new tables
    op.execute('''
    -- ai_models table
    CREATE TABLE ai_models (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        name VARCHAR(255) NOT NULL,
        version VARCHAR(50) NOT NULL,
        model_type VARCHAR(100) NOT NULL,
        is_baseline BOOLEAN DEFAULT FALSE,
        is_fine_tuned BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    -- training_pair_sets table (parent)
    CREATE TABLE training_pair_sets (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        pair_id VARCHAR(20) NOT NULL UNIQUE,
        user_prompt TEXT,
        system_prompt TEXT,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    -- generated_training_pairs table (child)
    CREATE TABLE generated_training_pairs (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        training_pair_set_id UUID REFERENCES training_pair_sets(id) ON DELETE CASCADE,
        ai_model_id UUID REFERENCES ai_models(id) ON DELETE CASCADE,
        prompt TEXT NOT NULL,
        topic VARCHAR(255),
        category VARCHAR(255),
        duration_seconds INT,
        score INT,
        target_audience VARCHAR(255),
        content_style VARCHAR(255),
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    -- generated_scenes table
    CREATE TABLE generated_scenes (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        training_pair_id UUID REFERENCES generated_training_pairs(id) ON DELETE CASCADE,
        scene_number INT,
        scene_type VARCHAR(100),
        timestamp VARCHAR(50),
        text_overlay TEXT,
        voiceover TEXT,
        visual TEXT,
        tip TEXT,
        order_index INT,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    CREATE UNIQUE INDEX idx_generated_scenes_training_pair 
    ON generated_scenes (training_pair_id, order_index) WHERE deleted_at IS NULL;

    -- generated_hook_variants table
    CREATE TABLE generated_hook_variants (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        training_pair_id UUID REFERENCES generated_training_pairs(id) ON DELETE CASCADE,
        hook_variant INT,
        scene_number INT,
        scene_type VARCHAR(100),
        timestamp VARCHAR(50),
        text_overlay TEXT,
        voiceover TEXT,
        visual TEXT,
        tip TEXT,
        order_index INT,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    CREATE UNIQUE INDEX idx_generated_hook_variants_training_pair 
    ON generated_hook_variants (training_pair_id, order_index) WHERE deleted_at IS NULL;

    -- user_preferences table
    CREATE TABLE user_preferences (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        user_id UUID REFERENCES users(id) ON DELETE SET NULL,
        training_pair_set_id UUID REFERENCES training_pair_sets(id) ON DELETE CASCADE,
        selected_training_pair_id UUID REFERENCES generated_training_pairs(id) ON DELETE CASCADE,
        preference_reason TEXT,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    CREATE INDEX idx_user_preferences_user_id 
    ON user_preferences (user_id) WHERE deleted_at IS NULL;

    CREATE INDEX idx_user_preferences_training_pair 
    ON user_preferences (selected_training_pair_id) WHERE deleted_at IS NULL;
               
    CREATE INDEX idx_user_preferences_training_pair_set 
    ON user_preferences (training_pair_set_id) WHERE deleted_at IS NULL;
    ''')


def downgrade() -> None:
    op.execute('''
    DROP INDEX IF EXISTS idx_user_preferences_training_pair;
    DROP INDEX IF EXISTS idx_user_preferences_user_id;
    DROP INDEX IF EXISTS idx_generated_hook_variants_training_pair;
    DROP INDEX IF EXISTS idx_generated_scenes_training_pair;

    DROP TABLE IF EXISTS user_preferences;
    DROP TABLE IF EXISTS generated_hook_variants;
    DROP TABLE IF EXISTS generated_scenes;
    DROP TABLE IF EXISTS generated_training_pairs;
    DROP TABLE IF EXISTS training_pair_sets;
    DROP TABLE IF EXISTS ai_models;
    ''')