"""Initial migration

Revision ID: 9df287856594
Revises: 
Create Date: 2025-06-15 18:41:41.893794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9df287856594'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    -- Enable uuid-ossp extension (PostgreSQL)
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

    -- Users table
    CREATE TABLE users (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        username VARCHAR(50) UNIQUE NOT NULL,
        full_name VARCHAR(100),
        team VARCHAR(100),
        password TEXT NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    CREATE UNIQUE INDEX idx_users_username ON users USING btree (username)
    WHERE deleted_at IS NULL;

    -- Training pairs
    CREATE TABLE training_pairs (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        pair_id VARCHAR(20) UNIQUE NOT NULL,
        topic VARCHAR(255),
        category VARCHAR(255),
        duration_seconds INT,
        score INT,
        user_prompt TEXT,
        system_prompt TEXT,
        target_audience VARCHAR(255),
        content_style VARCHAR(255),
        status VARCHAR(20) DEFAULT 'QUEUE' NOT NULL,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );
               
    CREATE UNIQUE INDEX idx_training_pairs_pair_id ON training_pairs USING btree (pair_id)
    WHERE deleted_at IS NULL;

    -- Hashtags table
    CREATE TABLE hashtags (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        name VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );
    
    CREATE UNIQUE INDEX idx_hashtags_name ON hashtags USING btree (name)
    WHERE deleted_at IS NULL;

    -- Many-to-many linking table
    CREATE TABLE training_pair_hashtags (
        training_pair_id UUID REFERENCES training_pairs(id) ON DELETE CASCADE,
        hashtag_id UUID REFERENCES hashtags(id) ON DELETE CASCADE,
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP,
        PRIMARY KEY (training_pair_id, hashtag_id)
    );

    CREATE UNIQUE INDEX idx_training_pair_hashtags ON training_pair_hashtags
    USING btree (training_pair_id, hashtag_id) WHERE deleted_at IS NULL;

    -- Hook variants
    CREATE TABLE hook_variants (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        training_pair_id UUID REFERENCES training_pairs(id) ON DELETE CASCADE,
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

    CREATE UNIQUE INDEX idx_hook_variants_training_pair ON hook_variants
    USING btree (training_pair_id, order_index) WHERE deleted_at IS NULL;

    -- Scenes
    CREATE TABLE scenes (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        training_pair_id UUID REFERENCES training_pairs(id) ON DELETE CASCADE,
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
               
    CREATE UNIQUE INDEX idx_scenes_training_pair ON scenes
    USING btree (training_pair_id, order_index) WHERE deleted_at IS NULL;

    -- Review actions
    CREATE TABLE review_actions (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        training_pair_id UUID REFERENCES training_pairs(id) ON DELETE CASCADE,
        user_id UUID REFERENCES users(id) ON DELETE SET NULL,
        action VARCHAR(20) CHECK (action IN ('APPROVED', 'REJECTED', 'SKIPPED', 'QUEUE')),
        notes TEXT,
        action_time TIMESTAMP DEFAULT now(),
        created_at TIMESTAMP DEFAULT now(),
        created_by VARCHAR(100) DEFAULT 'SYSTEM',
        updated_at TIMESTAMP DEFAULT now(),
        updated_by VARCHAR(100) DEFAULT 'SYSTEM',
        deleted_at TIMESTAMP
    );

    CREATE INDEX idx_review_actions_training_pair ON review_actions
    USING btree (training_pair_id, action_time) WHERE deleted_at IS NULL;
               
    ''')


def downgrade() -> None:
    op.execute('''
    -- Drop indexes first
    DROP INDEX IF EXISTS idx_review_actions_training_pair;
    DROP INDEX IF EXISTS idx_scenes_training_pair;
    DROP INDEX IF EXISTS idx_hook_variants_training_pair;
    DROP INDEX IF EXISTS idx_training_pair_hashtags;
    DROP INDEX IF EXISTS idx_hashtags_name;
    DROP INDEX IF EXISTS idx_training_pairs_pair_id;
    DROP INDEX IF EXISTS idx_users_username;

    -- Drop tables in reverse dependency order
    DROP TABLE IF EXISTS review_actions;
    DROP TABLE IF EXISTS scenes;
    DROP TABLE IF EXISTS hook_variants;
    DROP TABLE IF EXISTS training_pair_hashtags;
    DROP TABLE IF EXISTS hashtags;
    DROP TABLE IF EXISTS training_pairs;
    DROP TABLE IF EXISTS users;

    -- Remove extension (optional, safe to ignore if not needed)
    DROP EXTENSION IF EXISTS "uuid-ossp";
    ''')
