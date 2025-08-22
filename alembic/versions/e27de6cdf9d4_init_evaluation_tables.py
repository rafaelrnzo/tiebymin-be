"""init evaluation tables

Revision ID: e27de6cdf9d4
Revises: d34bd9316247
Create Date: 2025-07-28 17:08:52.673089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e27de6cdf9d4'
down_revision: Union[str, None] = 'd34bd9316247'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    -- Fine tune models table
    CREATE TABLE fine_tune_models (
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

    -- Generated training pairs table
    CREATE TABLE generated_training_pairs (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        ai_model_id UUID REFERENCES fine_tune_models(id) ON DELETE CASCADE,
        prompt TEXT NOT NULL,
        pair_id VARCHAR(20) UNIQUE NOT NULL,
        topic VARCHAR(255),
        category VARCHAR(255),
        duration_seconds INT,
        score INT,
        user_prompt TEXT,
        system_prompt TEXT,
        target_audience VARCHAR(255),
        content_style VARCHAR(255),
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    CREATE UNIQUE INDEX idx_generated_training_pairs_pair_id ON generated_training_pairs 
    USING btree (pair_id) WHERE deleted_at IS NULL;

    -- Generated hook variants table
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

    CREATE UNIQUE INDEX idx_generated_hook_variants_training_pair ON generated_hook_variants
    USING btree (training_pair_id, order_index) WHERE deleted_at IS NULL;

    -- Generated scenes table
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

    CREATE UNIQUE INDEX idx_generated_scenes_training_pair ON generated_scenes
    USING btree (training_pair_id, order_index) WHERE deleted_at IS NULL;

    -- User preferences table
    CREATE TABLE user_preferences (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        user_id UUID REFERENCES users(id) ON DELETE SET NULL,
        selected_training_pair_id UUID REFERENCES generated_training_pairs(id) ON DELETE CASCADE,
        preference_reason TEXT,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    CREATE INDEX idx_user_preferences_user_id ON user_preferences
    USING btree (user_id) WHERE deleted_at IS NULL;

    CREATE INDEX idx_user_preferences_training_pair ON user_preferences
    USING btree (selected_training_pair_id) WHERE deleted_at IS NULL;
    ''')


def downgrade() -> None:
    op.execute('''
    -- Drop indexes first
    DROP INDEX IF EXISTS idx_user_preferences_training_pair;
    DROP INDEX IF EXISTS idx_user_preferences_user_id;
    DROP INDEX IF EXISTS idx_generated_scenes_training_pair;
    DROP INDEX IF EXISTS idx_generated_hook_variants_training_pair;
    DROP INDEX IF EXISTS idx_generated_training_pairs_pair_id;

    -- Drop tables in reverse dependency order
    DROP TABLE IF EXISTS user_preferences;
    DROP TABLE IF EXISTS generated_scenes;
    DROP TABLE IF EXISTS generated_hook_variants;
    DROP TABLE IF EXISTS generated_training_pairs;
    DROP TABLE IF EXISTS fine_tune_models;
    ''')
