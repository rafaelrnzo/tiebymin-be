"""Insert Initial Training Data

Revision ID: d34bd9316247
Revises: 284d517ead4a
Create Date: 2025-07-22 18:28:13.396072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd34bd9316247'
down_revision: Union[str, None] = '284d517ead4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bbf1c073-6da1-4eec-b861-23571040662c'::uuid, 'SCR250720IOAU', 'mie goreng rumahan', 'Cooking', 20, 90, 'Script resep mie goreng rumahan anti gagal.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('843b2db8-a147-4c29-8644-ff8fca2901d9'::uuid, 'SCR2507207FWW', 'tips meal prep sehat', 'Health & Fitness', 20, 90, 'Buatkan script tips meal prep sehat untuk seminggu.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c62c7c57-75d9-44c0-9bb1-4d2196cd8c96'::uuid, 'SCR250720F5ZJ', 'dalgona coffee', 'Cooking', 20, 90, 'Script TikTok cara bikin dalgona coffee yang creamy.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1dd06f8f-2463-4256-a2b4-aeab6fac32c8'::uuid, 'SCR250720SWTS', 'steak medium-rare', 'Cooking', 20, 90, 'Cara memasak steak medium-rare di rumah—tolong script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ab4f5488-36a4-4743-9cd5-a46601285cff'::uuid, 'SCR250720GUHZ', 'tumis brokoli 5 menit', 'Cooking', 25, 90, 'Recipe hack tumis brokoli 5 menit—bikin video script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e56a9ad1-940c-47b9-b9ea-0930fb058d64'::uuid, 'SCR250720HXEK', '3 saus sambal homemade', 'Cooking', 20, 90, 'Script ‘3 saus sambal homemade’ yang cepat dibuat.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('02d40f41-4ed1-4d1b-abd0-76f8110e6ef3'::uuid, 'SCR250720D5NL', 'Oreo Mug Cake', 'Cooking', 90, 85, 'Buatkan script dessert oreo mug cake 90 detik.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c18b9328-0ecc-48ef-8451-70f12c3574c6'::uuid, 'SCR250720XTWO', 'Tips memilih pisau dapur & cara merawatnya', 'Cooking', 20, 90, 'Tips memilih pisau dapur & cara merawatnya—script, please.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('19bd4e57-f36b-4176-b82a-0a5e5cda024a'::uuid, 'SCR250720PHQT', 'tips produktivitas', 'Produktivitas', 20, 90, 'Buatkan script tips produktivitas', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c46e1d12-f30c-4abb-a204-ccd02a0d0c2b'::uuid, 'SCR250720Z5VU', 'dampak AI terhadap dunia pendidikan', 'Education', 20, 90, 'Content mengenai dampak AI terhadap dunia pendidikan', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('fe57a17a-d5c8-4d02-b57c-b5e41d79dc8f'::uuid, 'SCR250720Q7NX', 'manajemen waktu mahasiswa', 'Productivity', 20, 90, 'Buatkan script tips manajemen waktu untuk mahasiswa.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('203268ac-3c9f-4db6-9689-fc4e51818998'::uuid, 'SCR2507208A05', 'menghilangkan prokrastinasi', 'Productivity', 20, 90, 'Script TikTok tentang cara menghilangkan prokrastinasi.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1141bbe1-749c-4081-a55b-8ec509ffef4a'::uuid, 'SCR25072083GS', 'Tips membuat to-do list harian yang efektif', 'Productivity', 20, 90, 'Tips membuat to-do list harian yang efektif—tolong jadikan video script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('69b96c49-437f-4d86-ba7f-c1bb35899c93'::uuid, 'SCR250720WQBC', 'teknik Pomodoro', 'Productivity', 20, 90, 'Script singkat soal teknik Pomodoro biar fokus belajar.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('09407675-a975-4315-892a-606cd413f95c'::uuid, 'SCR250720ET7K', 'mengatur workspace', 'Productivity', 25, 85, 'Bagaimana cara mengatur workspace supaya lebih produktif? Buatkan script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('2ccf569a-a37b-475b-a36c-ffe9b06ce393'::uuid, 'SCR2507200CE4', 'Tips bangun pagi jam 5 subuh untuk pekerja remote', 'Productivity', 20, 90, 'Tips bangun pagi jam 5 subuh untuk pekerja remote, script TikTok please.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('12def5a0-1dc7-4f12-a42d-6fa7a1aa6329'::uuid, 'SCR250720SJ63', 'kebiasaan kecil yang bikin produktivitas naik 2×', 'Productivity', 20, 90, 'Script: kebiasaan kecil yang bikin produktivitas naik 2×.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e52583e6-d622-411a-b8f3-c053c487c8f5'::uuid, 'SCR250720DPS1', 'digital detox 24 jam', 'Health & Wellness', 20, 90, 'Buatkan video script ‘digital detox 24 jam’ yang engaging.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cb9cdeaf-5a08-4790-892c-bea7a1af8ff1'::uuid, 'SCR2507207LN1', 'merencanakan minggu kerja', 'Productivity', 20, 90, 'Script TikTok untuk merencanakan minggu kerja di hari Minggu malam.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b23d8585-5dca-4523-b6a8-21568e3575bf'::uuid, 'SCR250720IPJT', 'goal SMART', 'Produktivitas', 20, 88, 'Cara menulis goal SMART yang realistis—mohon dijadikan script TikTok.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e4244740-d32f-4a7a-a3e5-cd833a22da47'::uuid, 'SCR250720A7WO', 'nasi goreng ala restoran', 'Cooking', 20, 90, 'Script TikTok tentang rahasia nasi goreng ala restoran.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('63990380-f319-4fbc-9671-0bcdda48de0a'::uuid, 'SCR250720YSSY', 'plating makanan aesthetic', 'Cooking', 20, 90, 'Cara plating makanan biar aesthetic untuk konten—tolong script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d76b5366-0a1f-4d59-a9bf-27ac38060b04'::uuid, 'SCR2507200TGW', '7-minute abs tanpa alat', 'Workout', 20, 90, 'Script workout 7-minute abs tanpa alat.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7b7675b9-cbb5-4343-82fe-ca20b9a434ee'::uuid, 'SCR250720W1E2', 'Tips stretching untuk pekerja kantoran', 'Kesehatan & Kebugaran', 20, 90, 'Tips stretching untuk pekerja kantoran—bikin video script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('76f5d625-a8b9-411a-a673-ae2e3dc0220b'::uuid, 'SCR250720A2UD', '5 gerakan HIIT pembakar kalori', 'Fitness', 20, 90, 'Script TikTok ‘5 gerakan HIIT’ pembakar kalori.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b2f59a20-2b30-44f4-91e4-be18b2781ecc'::uuid, 'SCR25072068UP', 'postur tubuh saat duduk', 'Health & Fitness', 20, 88, 'Cara menjaga postur tubuh saat duduk lama—tolong script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ae76d49e-e767-4ba5-835c-0275f51a141b'::uuid, 'SCR250720O372', 'latihan resistance band di rumah', 'Fitness', 20, 90, 'Script panduan pemula latihan resistance band di rumah.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a1f88c38-3111-460b-926a-f40eceecc15a'::uuid, 'SCR2507202WGB', 'challenge push-up 30 hari', 'Fitness', 20, 90, 'Buatkan script challenge push-up 30 hari.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('87694d20-0367-483f-8fda-8a36fc92bd80'::uuid, 'SCR2507207AFF', 'apa yang saya makan dalam sehari', 'Diet dan Nutrisi', 25, 90, 'Script ‘what I eat in a day’ versi diet seimbang.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0d75aaf9-f506-44e9-8e84-483905b1d5f9'::uuid, 'SCR250720PQY9', 'tips minum air cukup sehari', 'Health', 20, 90, 'Tips minum air cukup sehari—video script, please.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6020ff28-3774-40a6-904b-bdc0c225c1d3'::uuid, 'SCR250720T0TN', 'manfaat walk-meeting 15 menit', 'Productivity', 20, 90, 'Script TikTok tentang manfaat walk-meeting 15 menit.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9be732c8-4ffa-44d7-aec8-e2b72e187e2e'::uuid, 'SCR2507208O2G', 'cara meditasi 5 menit untuk pemula', 'Wellness', 20, 85, 'Cara meditasi 5 menit untuk pemula—tolong buat script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bb8648d8-a0ee-4e46-873e-90b5b38bb6b3'::uuid, 'SCR250720L298', 'smartphone flagship terbaru', 'Tech', 20, 90, 'Script review cepat smartphone flagship terbaru.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d3264700-2a3c-43a1-85ea-e3031de81903'::uuid, 'SCR250720EJ3T', 'tips merawat baterai laptop', 'Teknologi', 20, 90, 'Buatkan video script tips merawat baterai laptop.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d19e09e7-4a74-4fdc-8bdb-93549be138d4'::uuid, 'SCR250720D4TV', 'AI tool gratis', 'Teknologi', 20, 90, 'Script TikTok: 3 AI tool gratis yang wajib dicoba.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('efade350-2301-45b5-ba6c-ebd43d641154'::uuid, 'SCR250720IW5U', 'setting kamera smartphone untuk video sinematik', 'Teknologi', 20, 90, 'Cara setting kamera smartphone untuk video sinematik—script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('11653dd9-475c-4dd4-8fb5-6615d41c349d'::uuid, 'SCR250720O1D9', 'USB-C vs Lightning', 'Tech', 20, 90, 'Script penjelasan singkat tentang USB-C vs Lightning.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bce52fac-f6e0-49ec-8fba-5912239f0602'::uuid, 'SCR25072068S2', 'shortcut Windows 11', 'Productivity', 20, 90, 'Script tips mengetik cepat pakai shortcut Windows 11.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('62c77009-1b98-4205-a2fe-ed07e50989d1'::uuid, 'SCR25072090ZZ', 'Unboxing dan first impression earbuds ANC', 'Tech', 20, 90, 'Unboxing dan first impression earbuds ANC—tolong script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ba73159c-804c-4da2-9190-82b186364480'::uuid, 'SCR2507201MWG', 'cara kerja wireless charging', 'Tech', 20, 90, 'Script TikTok jelaskan cara kerja wireless charging.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bd9963e3-b98d-45d8-ada3-b1d1c096dddb'::uuid, 'SCR250720L2OA', 'aplikasi catatan terbaik di Android', 'Productivity', 20, 90, '3 aplikasi catatan terbaik di Android—bikin script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('657c5234-1077-4849-ac4a-8e8b9475dfe3'::uuid, 'SCR250720XYJZ', 'backup data ke cloud', 'Tech', 20, 90, 'Script tutorial backup data penting ke cloud secara otomatis.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e9e086c9-d0f1-4806-8f0e-9954f4d68d27'::uuid, 'SCR250720P7UE', 'menabung 50-30-20 rule', 'Finance', 20, 90, 'Script tips menabung 50-30-20 rule untuk fresh graduate.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6785cc33-38da-4aef-b0d3-7892d16368fb'::uuid, 'SCR250720797U', 'perbedaan saham dan reksa dana', 'Keuangan', 20, 90, 'Buatkan script TikTok: perbedaan saham & reksa dana.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c2d2cd63-e6ad-4ba0-9cbb-007dda8149bb'::uuid, 'SCR250720WA2V', 'anggaran bulanan di spreadsheet', 'Productivity', 20, 90, 'Cara membuat anggaran bulanan di spreadsheet—tolong script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7166f4f6-cef1-4061-9f75-d2c6e97cd09e'::uuid, 'SCR250720OMAA', 'emergency fund', 'Keuangan', 20, 90, 'Script singkat tentang emergency fund dan cara memulainya.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c1ecdfdd-fa39-4767-9864-7b23d51f98b6'::uuid, 'SCR250720RT5X', 'kesalahan finansial umum di usia 20-an', 'Keuangan', 20, 90, 'Script TikTok: kesalahan finansial umum di usia 20-an.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ca27451b-a8ba-46e2-8bba-e75b75430b5f'::uuid, 'SCR250720XPDX', 'investasi emas digital aman', 'Investasi', 25, 90, 'Cara investasi emas digital aman—bikin video script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d9d718c8-8a6f-4ea1-b06d-618e90208e42'::uuid, 'SCR250720WP09', 'belanja online hemat', 'Shopping', 25, 90, 'Tips belanja online hemat pakai aplikasi cashback—script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'QUEUE', '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e004d6d6-e2ef-43b0-9508-c0594cacb4b1'::uuid, 'SCR250720U68Y', 'strategi melunasi utang dengan metode snowball', 'Keuangan', 20, 90, 'Script TikTok strategi melunasi utang dengan metode snowball. ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'REJECTED', '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('098304a2-a8f2-40fb-8322-fea897f57848'::uuid, 'SCR250720SBYS', 'compound interest', 'Finance', 20, 90, 'Penjelasan singkat compound interest—tolong script.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'APPROVED', '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', NULL);
        INSERT INTO training_pairs
        (id, pair_id, topic, category, duration_seconds, score, user_prompt, system_prompt, target_audience, content_style, status, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('56ee3216-38e7-4442-b4fb-849d651e96cb'::uuid, 'SCR2507204ZMK', 'budgeting ala amplop', 'Finance', 60, 90, 'Script ‘budgeting ala amplop’ dalam 60 detik.
        ', 'You are an expert TikTok script writer. Create engaging video scripts based on user requests.

        CRITICAL REQUIREMENTS:
        1. Focus completely on the user''s specific request
        2. Create relevant hooks that introduce the specific topic
        3. Use id language naturally
        4. Make it engaging for TikTok audience
        5. OUTPUT MUST BE VALID JSON - no additional text

        JSON OUTPUT FORMAT REQUIRED:
        {
        "type": "video_script",
        "generated_at": "ISO timestamp",
        "duration_estimate": "15-25s",
        "performance_score": 85,
        "target_audience": "Gen Z dan Millennial Indonesia",
        "content_style": "Engaging dan informatif",
        "category": "Category topic (e.g., Productivity, Cooking, Tech)",
        "trending_elements": ["Quick tips", "Visual demonstration", "Strong CTA"],
        "primary_keyword": "topic from user request",
        "data": {
            "hooks": [
            // 2-5 hook variants, all with scene_number: 1
            {
                "hook_variant": 1,
                "scene_number": 1,
                "scene_type": "Hook",
                "timestamp": "0-3s",
                "text_overlay": "MENARIK!",
                "voiceover": "HAI GUYS! [excited tone] Kalian tau gak sih...PANJANG dan DETAIL dengan CAPSLOCK untuk penekanan...",
                "visual": "Extreme close-up mata dengan soft lighting dari ring light, slow zoom out ke medium shot...",
                "tip": "Start with high energy and eye contact"
            }
            ],
            "script_body": [
            // Main content scenes starting from scene_number: 2
            {
                "scene_number": 2,
                "scene_type": "Main Content",
                "timestamp": "3-8s",
                "text_overlay": "RAHASIA #1",
                "voiceover": "Pertama guys, kalian harus tau bahwa...PANJANG dan DETAIL...",
                "visual": "Medium shot dengan gentle pan right menunjukkan...DETAIL VISUAL...",
                "tip": "Use hand gestures to emphasize points"
            }
            ]
        }
        }

        HOOK GENERATION RULES:
        - Generate 2-5 different hook variants
        - Each hook variant has hook_variant: 1, 2, 3, etc.
        - ALL hooks have scene_number: 1
        - Each hook should have different approach:
        * Hook 1: Question/Problem approach
        * Hook 2: Shocking fact/statistic approach  
        * Hook 3: Personal story/experience approach
        - timestamp for all hooks: "0-3s"

        SCRIPT BODY NUMBERING:
        - script_body scenes start from scene_number: 2
        - Continue sequentially: 2, 3, 4, 5, etc.

        VOICEOVER REQUIREMENTS:
        - Use CAPSLOCK for emphasis on important words
        - Use punctuation for pacing
        - 50-80 words minimum per scene
        - Include tone indicators like [excited], [serious]
        - Natural flow ready for recording

        VISUAL REQUIREMENTS:
        - Specify camera angles: extreme close-up, medium shot, wide shot
        - Detail camera movements: zoom, pan, tilt
        - Lighting specifics: ring light, natural light
        - Talent position and gestures
        - Background and props

        Remember: Output ONLY valid JSON, no additional text.', 'Gen Z dan Millennial Indonesia', 'Engaging dan informatif', 'REJECTED', '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', NULL);
               

        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('05b5a68e-4aad-42c7-9aef-9017896be7e5'::uuid, '19bd4e57-f36b-4176-b82a-0a5e5cda024a'::uuid, 1, 1, 'Hook', '0-3s', 'BINGUNG NAIKKAN PRODUKTIVITAS?', 'Hai guys! [excited tone] Apa kalian pernah merasa...waktu kalian terbuang sia-sia? Jangan khawatir, aku punya TIPS untuk kalian!', 'Extreme close-up wajah dengan ekspresi khawatir, lalu beralih ke medium shot menunjukkan kalender atau jam.', 'Start with an engaging expression and relatable question.', 1, '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7b2a45e4-ed28-4511-b8ae-a050cf3a7477'::uuid, '19bd4e57-f36b-4176-b82a-0a5e5cda024a'::uuid, 2, 1, 'Hook', '0-3s', 'STATISTIK MENAWAN!', 'Tahukah kalian bahwa...hanya 20% orang yang benar-benar produktif? [serious tone] Ayo kita ubah itu!', 'Wide shot dengan grafik statistik yang menunjukkan data produktivitas di layar.', 'Use compelling stats to grab attention.', 2, '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('dfc8e787-5ae9-43d0-ba01-08b8cc6670d6'::uuid, '19bd4e57-f36b-4176-b82a-0a5e5cda024a'::uuid, 3, 1, 'Hook', '0-3s', 'PENGALAMAN PRIBADI!', 'Dulu, aku sering merasa...tidak produktif sama sekali! [relatable tone] Tapi sekarang, ini yang aku lakukan!', 'Medium shot menunjukkan creator duduk di meja kerja dengan laptop dan catatan.', 'Share a personal experience to establish connection.', 3, '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('47966d75-26a3-48c1-a2d6-9dc5bca20037'::uuid, 'c46e1d12-f30c-4abb-a204-ccd02a0d0c2b'::uuid, 1, 1, 'Hook', '0-3s', 'PENGEN TAHU?', 'Hai, guys! [excited tone] Kalian pernah denger tentang DAMPAR AI di dunia pendidikan? Yuk kita kulik!', 'Extreme close-up wajah dengan latar belakang buku dan laptop, slow zoom out ke medium shot...', 'Start with an engaging facial expression', 1, '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6c7d0b5b-2ed8-452b-91e1-ebddb1779d2a'::uuid, 'c46e1d12-f30c-4abb-a204-ccd02a0d0c2b'::uuid, 2, 1, 'Hook', '0-3s', 'FAKTA MENARIK', 'Did you know? [serious tone] 60% siswa merasa AI MEMBANTU mereka belajar lebih efektif! Gimana ya cara kerjanya?', 'Wide shot dengan grafik animasi AI dan pendidikan muncul di layar...', 'Use gestures to emphasize statistics', 2, '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('598d3d7e-747a-44e5-9ffa-33af2a525da2'::uuid, 'c46e1d12-f30c-4abb-a204-ccd02a0d0c2b'::uuid, 3, 1, 'Hook', '0-3s', 'MOMEN PRIBADI', 'Jadi, pas aku belajar bahasa baru, aku pakai AI untuk PRAKTIK! [enthusiastic tone] Dan hasilnya luar biasa!', 'Medium shot menunjukkan talent belajar di meja dengan aplikasi AI di laptop...', 'Share a personal anecdote to connect', 3, '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e22d7bc6-34f4-471d-96c0-bfeb7508ffba'::uuid, 'fe57a17a-d5c8-4d02-b57c-b5e41d79dc8f'::uuid, 1, 1, 'Hook', '0-3s', 'BINGUNG NGATUR WAKTU?', 'Hai teman-teman! [excited tone] Kalian sering bingung ngatur waktu sebagai mahasiswa?', 'Extreme close-up wajah dengan ekspresi bingung, soft lighting dari ring light, slow zoom out ke medium shot.', 'Start with relatable expressions to grab attention.', 1, '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('21e5515f-dee0-49aa-918b-ee0906975fc7'::uuid, 'fe57a17a-d5c8-4d02-b57c-b5e41d79dc8f'::uuid, 2, 1, 'Hook', '0-3s', 'FAKTA MENARIK!', 'Tahukah kalian? [surprised tone] Mahasiswa yang punya manajemen waktu yang baik cenderung lebih sukses!', 'Wide shot di depan meja belajar dengan berbagai catatan, gesturing dengan tangan.', 'Use surprising statistics to engage viewers.', 2, '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('54b3449e-be6e-486e-a8e6-8f795607dd0e'::uuid, 'fe57a17a-d5c8-4d02-b57c-b5e41d79dc8f'::uuid, 3, 1, 'Hook', '0-3s', 'PENGALAMAN PRIBADI!', 'Aku pernah loh, [nostalgic tone] ngerasain panik karena tugas menumpuk. Tapi, ada cara mudahnya!', 'Medium shot duduk di meja kerja dengan tumpukan buku, tampak merenung.', 'Share personal stories for relatability.', 3, '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4f594818-8609-4241-b27c-0914f5acb8d1'::uuid, '203268ac-3c9f-4db6-9689-fc4e51818998'::uuid, 1, 1, 'Hook', '0-3s', 'TERLALU SERING MENUNDA?', 'Hai guys! [excited tone] Kalian sering ngerasa...PROKRASTINASI itu mengganggu produktivitas?', 'Extreme close-up wajah dengan ekspresi bingung, slow zoom out ke medium shot, menampilkan lemari yang berantakan.', 'Mulai dengan ekspresi wajah yang mengundang rasa penasaran.', 1, '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a5f1be39-d83b-455d-8b1f-0a434c73d72e'::uuid, '203268ac-3c9f-4db6-9689-fc4e51818998'::uuid, 2, 1, 'Hook', '0-3s', 'FAKTA MENARIK!', 'Tahukah kalian? [serious tone] 70% orang muda mengalami PROKRASTINASI, loh!', 'Medium shot dengan grafik visual statistik yang menarik, latar belakang dinamis.', 'Gunakan grafik untuk menangkap perhatian penonton.', 2, '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7286f3ab-e10a-41c0-9957-e5de3c741bde'::uuid, '203268ac-3c9f-4db6-9689-fc4e51818998'::uuid, 3, 1, 'Hook', '0-3s', 'PERNAH MERASAKAN?', 'Dulu, aku juga sering prokrastinasi! [nostalgic tone] Sampai akhirnya aku menemukan cara untuk mengatasinya!', 'Medium shot dengan potongan video pengalaman pribadi, menunjukkan momen saat menunda pekerjaan.', 'Berikan sentuhan pribadi untuk menghubungkan dengan penonton.', 3, '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d48775b6-cd61-4b71-9ef7-59b8e046db98'::uuid, '1141bbe1-749c-4081-a55b-8ec509ffef4a'::uuid, 1, 1, 'Hook', '0-3s', 'BINGUNG GAK BISA FOKUS?', 'Hai guys! [excited tone] Pasti pernah bingung mau mulai dari mana hari ini, kan? Yuk, kita atasi ini dengan TO-DO LIST!', 'Extreme close-up wajah dengan ekspresi bingung, lalu zoom out ke meja kerja berantakan.', 'Start with a relatable problem.', 1, '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('888bd0dd-2a25-49d1-a1b0-5e643e97520c'::uuid, '1141bbe1-749c-4081-a55b-8ec509ffef4a'::uuid, 2, 1, 'Hook', '0-3s', 'KISAH SEDIH!', 'Dulu, aku selalu lupa tugas-tugas penting. [serious tone] Tapi sekarang, TO-DO LIST adalah penyelamat hidupku!', 'Medium shot dengan flashback ke situasi kacau, lalu kembali ke senyum di meja kerja rapi.', 'Share a personal experience.', 2, '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a997ab15-fe3a-4580-ae71-1bb6050b8320'::uuid, '1141bbe1-749c-4081-a55b-8ec509ffef4a'::uuid, 3, 1, 'Hook', '0-3s', 'TIPS MUDAH!', 'Hey! [excited tone] Mau tahu cara gampang bikin TO-DO LIST harian yang EFEKTIF? Let''s go!', 'Wide shot di ruang kerja dengan notebook terbuka dan alat tulis di sekeliling.', 'Create excitement for the upcoming content.', 3, '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7f08b2f0-705a-494d-b637-2d806ba0b747'::uuid, '69b96c49-437f-4d86-ba7f-c1bb35899c93'::uuid, 1, 1, 'Hook', '0-3s', 'KALIAN SUSAH FOKUS?', 'Hai guys! [excited tone] Apakah kalian sering merasa susah fokus saat belajar?', 'Extreme close-up wajah dengan ekspresi kebingungan, lalu zoom out menunjukkan buku berserakan di meja.', 'Start with a relatable question to connect with viewers', 1, '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ddfbf031-3d9d-4e8b-920e-485d92c43af1'::uuid, '69b96c49-437f-4d86-ba7f-c1bb35899c93'::uuid, 2, 1, 'Hook', '0-3s', 'FAKTA MENARIK!', 'Guys, tau gak sih? Rata-rata kita hanya bisa fokus 25 menit sebelum capek! [serious tone]', 'Quick cut to a timer ticking down from 25 minutes on a phone screen.', 'Use shocking stats to grab attention', 2, '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('db888acc-2986-4eda-91fd-8ea66e80297b'::uuid, '69b96c49-437f-4d86-ba7f-c1bb35899c93'::uuid, 3, 1, 'Hook', '0-3s', 'PENGALAMAN PRIBADI...', 'Dulu, aku juga mengalami hal yang sama! [narrative tone] Sampai aku coba teknik Pomodoro ini...', 'Wide shot menunjukkan orang yang frustrasi belajar, kemudian berubah menjadi fokus saat menggunakan timer.', 'Share a personal experience to build trust', 3, '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bc97b403-87ea-4a97-9ea7-797c7ff35bd6'::uuid, '09407675-a975-4315-892a-606cd413f95c'::uuid, 1, 1, 'Hook', '0-3s', 'PRODUKTIVITAS RAHASIA!', 'Hai guys! Kalian tau gak sih...BAGAIMANA cara mengatur WORKSPACE agar lebih PRODUKTIF?', 'Extreme close-up wajah dengan ekspresi penasaran, diiringi pencahayaan lembut dari ring light...', 'Start with an engaging facial expression', 1, '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('201590ef-12e4-4f0c-a249-ef6471197401'::uuid, '09407675-a975-4315-892a-606cd413f95c'::uuid, 2, 1, 'Hook', '0-3s', 'BAGAIAMANA CARA SUKSES?', 'Ternyata guys, 80% orang yang teratur dalam workspace-nya lebih PRODUKTIF! Mau tau caranya?', 'Medium shot dengan latar belakang workspace yang berantakan, menunjukkan kepusingan...', 'Use a surprised expression to emphasize the statistic', 2, '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('3e3f4f0c-67b9-4271-8889-acb715f8d3b0'::uuid, '09407675-a975-4315-892a-606cd413f95c'::uuid, 3, 1, 'Hook', '0-3s', 'PERUBAHAN MUDAH!', 'Aku dulu juga sering bingung, tapi setelah merapikan workspace, PRODUKTIVITASku meningkat drastis!', 'Wide shot dari workspace yang rapi dan berantakan, beralih ke rapi secara cepat...', 'Share a relatable personal story', 3, '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('77985cf5-ce9e-4c2c-89fe-a7177620d5a4'::uuid, '2ccf569a-a37b-475b-a36c-ffe9b06ce393'::uuid, 1, 1, 'Hook', '0-3s', 'SIAP MENJADI MORNING PERSON?', 'Hai guys! [excited tone] Kalian pernah bingung gimana caranya BANGUN PAGI jam 5 SUBUH? Yuk, simak tipsnya!', 'Extreme close-up wajah dengan ekspresi semangat, dilanjutkan zoom out ke medium shot berpose energik.', 'Start with an enthusiastic expression.', 1, '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('54f80318-3852-4aa5-9778-5e92a0cbecbd'::uuid, '2ccf569a-a37b-475b-a36c-ffe9b06ce393'::uuid, 2, 1, 'Hook', '0-3s', 'GEN Z JUGA BISA!', 'Kalian tau gak? [shocking tone] Bangun pagi ternyata bisa meningkatkan PRODUKTIVITAS hingga 30%! Gimana caranya?', 'Medium shot dengan grafik animasi produktivitas yang meningkat.', 'Use visuals to highlight the statistic.', 2, '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e1a685fa-18dd-4dbf-ad0d-7f0c4918b0bc'::uuid, '2ccf569a-a37b-475b-a36c-ffe9b06ce393'::uuid, 3, 1, 'Hook', '0-3s', 'KESEL GAK BANGUN PAGI?', 'Aku dulu juga kesulitan bangun pagi... [personal tone] Tapi sekarang aku punya TRIK JITU buat kalian!', 'Wide shot di tempat tidur, menunjukkan transisi dari gelap ke terang saat bangun.', 'Show relatable experience.', 3, '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b7d15004-7cf8-4152-bf22-8b448b351a25'::uuid, '12def5a0-1dc7-4f12-a42d-6fa7a1aa6329'::uuid, 1, 1, 'Hook', '0-3s', 'Tingkatkan Produktivitasmu!', 'HAI GUYS! [excited] Kalian tau gak sih ada kebiasaan KECIL yang bisa bikin PRODUKTIVITAS kalian naik 2×?', 'Extreme close-up wajah dengan ekspresi antusias, background sederhana dan cerah.', 'Mulai dengan senyuman dan energi positif.', 1, '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a670cc88-13c8-44d1-80f9-4b8e4b1a80e2'::uuid, '12def5a0-1dc7-4f12-a42d-6fa7a1aa6329'::uuid, 2, 1, 'Hook', '0-3s', 'Kamu Harus Tahu!', 'DENGAR INI! [serious] Penelitian menunjukkan bahwa kebiasaan kecil bisa meningkatkan produktivitas kalian hingga DUA KALI lipat!', 'Close-up dengan grafik animasi tentang produktivitas, dan pergerakan tangan untuk menekankan grafik.', 'Gunakan nada suara yang dramatis.', 2, '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6ce0f94c-7d26-46f4-a4d8-bb7a2b7e4cb4'::uuid, '12def5a0-1dc7-4f12-a42d-6fa7a1aa6329'::uuid, 3, 1, 'Hook', '0-3s', 'Kebiasaan Kecil', 'Ceritanya, aku mulai fokus pada kebiasaan kecil setiap hari... dan hasilnya? [excited] Produktivitasku meningkat DUA KALI lipat!', 'Medium shot dengan latar belakang ruangan kerja yang tertata rapi.', 'Tunjukkan ekspresi kekaguman saat bercerita.', 3, '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a127e574-2328-4a17-9f29-6d0d8e9a702c'::uuid, 'e52583e6-d622-411a-b8f3-c053c487c8f5'::uuid, 1, 1, 'Hook', '0-3s', 'SIAP UNTUK DETOX?', 'Hai Guys! [excited tone] Pernah denger tentang DIGITAL DETOX? Yuk kita coba 24 jam tanpa gadget!', 'Extreme close-up wajah dengan ekspresi antusias, slow zoom out menuju medium shot.', 'Maintain eye contact for engagement.', 1, '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('dec92cca-f794-40d9-a309-21e964926888'::uuid, 'e52583e6-d622-411a-b8f3-c053c487c8f5'::uuid, 2, 1, 'Hook', '0-3s', '100% TANPA GADGET!', 'Statistik menunjukkan, 70% dari kita butuh digital detox! Bayangkan 24 jam bebas dari semua gadget…', 'Medium shot dengan grafik di layar menunjukkan statistik penggunaan gadget.', 'Use visuals to emphasize the statistic.', 2, '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e78a4f44-7605-43df-817f-02921e553a09'::uuid, 'e52583e6-d622-411a-b8f3-c053c487c8f5'::uuid, 3, 1, 'Hook', '0-3s', 'MOMEN YANG TEPAT!', 'Jadi, kemarin saya coba detox digital! [personal tone] Dan wow, saya merasa lebih segar dan produktif!', 'Medium shot dengan background alami, menunjukkan keindahan alam saat detox.', 'Share a vivid personal experience.', 3, '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bf131b0a-902f-470f-9a8b-b0d60b1c5311'::uuid, 'cb9cdeaf-5a08-4790-892c-bea7a1af8ff1'::uuid, 1, 1, 'Hook', '0-3s', 'SIAP UNTUK MINGGU YANG MENENTANG?', 'Hai guys! [excited tone] Kalian udah siap untuk menghadapi minggu kerja? Yuk, kita rencanakan bareng-bareng!', 'Close-up wajah dengan senyuman, di sekitar meja kerja yang tertata rapi.', 'Mulai dengan senyuman dan energik', 1, '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('8ae41e65-7e42-461f-ab88-d42d7c8f104d'::uuid, 'cb9cdeaf-5a08-4790-892c-bea7a1af8ff1'::uuid, 2, 1, 'Hook', '0-3s', 'MINGGU TANPA RENCANA = CHAOS!', 'Pernah gak sih kalian mengalami minggu tanpa rencana? [serious tone] Hasilnya pasti chaos! Yuk, kita atur!', 'Zoom out dari wajah ke tampilan meja kerja berantakan.', 'Tunjukkan efek negatif dari kurangnya perencanaan', 2, '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('877f2934-a4a1-4dd4-9963-0fca5eb7be8d'::uuid, 'cb9cdeaf-5a08-4790-892c-bea7a1af8ff1'::uuid, 3, 1, 'Hook', '0-3s', 'RITUAL SUNDAY NIGHT!', 'Malam Minggu udah jadi ritual aku untuk merencanakan minggu. [personal tone] Jadi lebih fokus dan siap! Gimana dengan kalian?', 'Wide shot dengan buku catatan terbuka dan alat tulis di meja.', 'Ciptakan suasana santai dan akrab', 3, '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e1ff57ab-9fa7-4091-9ee7-0e85f0ce698d'::uuid, 'b23d8585-5dca-4523-b6a8-21568e3575bf'::uuid, 1, 1, 'Hook', '0-3s', 'Tahu Goal SMART?', 'Hai guys! [excited tone] Kalian tahu gak sih, bagaimana CARA MENULIS GOAL yang REALISTIS dengan rumus SMART? Yuk simak!', 'Extreme close-up wajah dengan ekspresi antusias, lalu zoom out ke medium shot.', 'Tunjukkan semangat dan keterlibatan di wajah', 1, '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('fdb991d9-71c4-4741-8ac1-ad2e8d57485e'::uuid, 'b23d8585-5dca-4523-b6a8-21568e3575bf'::uuid, 2, 1, 'Hook', '0-3s', 'Fakta Menarik!', 'Kenyataannya, 92% orang tidak mencapai goal mereka. [serious tone] Tapi, dengan metode SMART, kamu bisa jadi bagian dari 8% yang berhasil!', 'Medium shot dengan grafik animasi yang menunjukkan statistik, penekanan pada kata ‘92%’ dengan zoom.', 'Gunakan grafik yang menarik untuk membahas statistik', 2, '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('22488df5-7cdc-4506-b9a7-fc9416082367'::uuid, 'b23d8585-5dca-4523-b6a8-21568e3575bf'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman Pribadi', 'Dulu, saya sering bingung menulis goal. [personal tone] Tapi setelah tahu SMART, goal saya jadi lebih jelas dan terarah!', 'Wide shot dengan latar belakang ruang kerja, gestur tangan menunjuk ke papan tulis.', 'Tampilkan kesan personal agar audience terhubung', 3, '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('58d69c12-0249-4667-bf24-2b1aa6388f3e'::uuid, 'bbf1c073-6da1-4eec-b861-23571040662c'::uuid, 1, 1, 'Hook', '0-3s', 'MIE GORENG ANTI GAGAL!', 'HAI TEMAN-TEMAN! [excited tone] Mau bikin MIE GORENG super enak dan anti gagal? Yuk, simak!', 'Extreme close-up wajah dengan ekspresi ceria, latar belakang dapur yang bersih dan terang, slow zoom out ke medium shot...', 'Gunakan ekspresi wajah yang ceria untuk menarik perhatian.', 1, '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cacde625-2118-44cd-b10a-33df9fefee2f'::uuid, 'bbf1c073-6da1-4eec-b861-23571040662c'::uuid, 2, 1, 'Hook', '0-3s', 'RAHASIA RESEP SEDERHANA!', 'Kalian tahu gak? MIE GORENG bisa jadi LEZAT hanya dengan beberapa BAHAN!', 'Wide shot dapur dengan bahan-bahan di atas meja, kamera sedikit berpindah kiri dan kanan...', 'Tampilkan semua bahan dengan jelas dan menarik.', 2, '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('62ba8aeb-6fdf-4bb9-be3e-2e70c74d7124'::uuid, 'bbf1c073-6da1-4eec-b861-23571040662c'::uuid, 3, 1, 'Hook', '0-3s', 'CEK RESEP RUMAHAN!', 'Dulu, aku juga sering gagal bikin MIE GORENG. Tapi sekarang, aku punya rahasia buat kalian!', 'Medium shot, menunjukkan tangan menunjuk pada mie kering, senyum lebar...', 'Gunakan gesture yang percaya diri.', 3, '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('caa09d3a-cf78-4de7-9fd5-5c5e5eb7f74d'::uuid, '843b2db8-a147-4c29-8644-ff8fca2901d9'::uuid, 1, 1, 'Hook', '0-3s', 'MEAL PREP MUDAH!', 'HEY GUYS! [excited tone] Mau tau cara MEAL PREP SEHAT buat seminggu? Yuk kita simak!', 'Extreme close-up wajah dengan ekspresi semangat, lalu zoom out untuk menunjukkan bahan-bahan di meja.', 'Start with high energy and an inviting smile.', 1, '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('94832541-131d-47c3-984f-aee9ec0cac1e'::uuid, '843b2db8-a147-4c29-8644-ff8fca2901d9'::uuid, 2, 1, 'Hook', '0-3s', 'HIDANGAN SEHAT!', 'DID YOU KNOW? [shocking tone] Meal prep bisa menghemat waktu memasak hingga 50%! [increase engagement]', 'Wide shot kitchen dengan jam menunjukan waktu yang terbuang saat memasak.', 'Use surprise statistics to grab attention.', 2, '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('be54ce73-100a-46a0-8959-2471aa914ac6'::uuid, '843b2db8-a147-4c29-8644-ff8fca2901d9'::uuid, 3, 1, 'Hook', '0-3s', 'CERITA MEAL PREP!', 'Aku dulu selalu bingung masak setiap hari, tapi setelah meal prep semua jadi lebih mudah! [personal tone]', 'Medium shot memegang wadah makanan sehat yang sudah dipersiapkan.', 'Share a personal anecdote for relatability.', 3, '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9c79b9ca-2a85-4e77-8560-71eda0ed5466'::uuid, 'c62c7c57-75d9-44c0-9bb1-4d2196cd8c96'::uuid, 1, 1, 'Hook', '0-3s', 'SIAPKAN DIRI!', 'Hai, guys! [excited tone] Pernah denger Dalgona Coffee? Ini adalah resepnya yang MUDAH dan CREAMY banget!', 'Extreme close-up wajah dengan senyum lebar, zoom out ke medium shot sambil memegang bahan.', 'Start with a bright smile and excitement', 1, '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('8fdcc001-72cf-43f1-86ec-74c15bf6d85d'::uuid, 'c62c7c57-75d9-44c0-9bb1-4d2196cd8c96'::uuid, 2, 1, 'Hook', '0-3s', 'PENYEGAR KOPI!', 'Ternyata, 45% orang Indonesia lebih suka kopi yang enak! [serious tone] Yuk, kita bikin Dalgona Coffee yang CREAMY!', 'Wide shot menunjukkan bahan-bahan di meja, dengan kopi di tengah.', 'Use a serious tone to emphasize the statistic', 2, '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('2588c9aa-4ab1-4fdd-a7c4-5caca22fdda6'::uuid, 'c62c7c57-75d9-44c0-9bb1-4d2196cd8c96'::uuid, 3, 1, 'Hook', '0-3s', 'KENANGAN MANIS!', 'Aku pertama kali coba Dalgona Coffee pas pandemi. [nostalgic tone] Ternyata bikin sendiri itu gampang banget!', 'Medium shot dengan gambar foto Dalgona Coffee di latar belakang, menunjukkan suasana nostalgia.', 'Share a relatable personal story', 3, '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e6811c93-6a21-49fb-92b6-886834b4b0be'::uuid, '1dd06f8f-2463-4256-a2b4-aeab6fac32c8'::uuid, 1, 1, 'Hook', '0-3s', 'STEAK SEMPURNA!', 'Hai guys! [excited tone] Kalian pengen tau cara memasak STEAK MEDIUM-RARE di rumah?!', 'Extreme close-up wajah dengan senyum lebar, soft lighting, menunjukkan semangat.', 'Start with a bright smile and high energy.', 1, '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('49b52220-5729-4f68-a45e-3df38f35962a'::uuid, '1dd06f8f-2463-4256-a2b4-aeab6fac32c8'::uuid, 2, 1, 'Hook', '0-3s', 'RAHASIA CHEF!', 'Tahukah kalian? [shocking tone] 80% orang menganggap steak MEDIUM-RARE itu paling enak!', 'Wide shot di dapur, dengan steak di meja, kamera berputar mengelilingi steak.', 'Use background visuals of ingredients.', 2, '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('25496078-3ca3-43f2-90e9-553fcc7040fd'::uuid, '1dd06f8f-2463-4256-a2b4-aeab6fac32c8'::uuid, 3, 1, 'Hook', '0-3s', 'BELAJAR BARENG!', 'Aku dulu juga bingung, [relatable tone] tapi sekarang aku bisa masak steak MEDIUM-RARE yang enak!', 'Medium shot dengan penampilan santai, memegang daging steak.', 'Connect with personal experience.', 3, '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9b3b7741-caa9-4b3c-b008-7b6f207ecc9a'::uuid, 'ab4f5488-36a4-4743-9cd5-a46601285cff'::uuid, 1, 1, 'Hook', '0-3s', '5 MENIT SAJA!', 'Hai guys! Mau tau cara masak TUMIS BROKOLI dalam 5 MENIT? Simpel dan ENAK!', 'Extreme close-up wajah excited dengan brokoli di tangan, slow zoom out.', 'Look enthusiastic to attract attention', 1, '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('19980212-df58-4615-a69c-2bd881411ee7'::uuid, 'ab4f5488-36a4-4743-9cd5-a46601285cff'::uuid, 2, 1, 'Hook', '0-3s', 'SEHAT & LEZAT!', 'Kalian tau gak? Brokoli bisa jadi menu SEHAT dan lezat dalam WAKTU SINGKAT!', 'Medium shot menampilkan brokoli segar dan bahan lainnya di meja.', 'Use engaging hand gestures', 2, '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('50665845-7f8c-434d-a855-82c2d3cab9c6'::uuid, 'ab4f5488-36a4-4743-9cd5-a46601285cff'::uuid, 3, 1, 'Hook', '0-3s', 'RESEP PRAKTIS!', 'Pernah bingung mau masak apa? Yuk, kita bikin TUMIS BROKOLI gampang dan cepat ini!', 'Wide shot menunjukkan dapur dan peralatan masak yang siap.', 'Make the viewer relate with your situation', 3, '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c298460e-f5f0-4ce4-93cf-147cae0ce08e'::uuid, 'e56a9ad1-940c-47b9-b9ea-0930fb058d64'::uuid, 1, 1, 'Hook', '0-3s', 'SAUS SAMBAL HOMEMADE!', 'Hai guys! Mau tau cara bikin 3 SAUS SAMBAL HOMEMADE yang gampang dan enak? Yuk simak!', 'Extreme close-up wajah excited, dengan latar belakang dapur yang bersih.', 'Tunjukkan semangat dan kepercayaan diri', 1, '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('29b77558-492b-402e-899d-aadf61e7a658'::uuid, 'e56a9ad1-940c-47b9-b9ea-0930fb058d64'::uuid, 2, 1, 'Hook', '0-3s', 'GAK PAKAI RIBET!', 'Tahukah kamu, bikin saus sambal itu GAK PERLU RIBET! Berikut 3 resep cepatnya!', 'Medium shot dari meja dapur, menampilkan bahan-bahan saus sambal.', 'Gunakan nada suara yang penuh percaya diri', 2, '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('05769486-91d0-4b6a-8bb2-d2bfa8f53d7a'::uuid, 'e56a9ad1-940c-47b9-b9ea-0930fb058d64'::uuid, 3, 1, 'Hook', '0-3s', 'KREATIF DI DAPUR!', 'Siapa bilang membuat saus sambal itu sulit? Ini pengalaman pertama saya, dan hasilnya WOW!', 'Wide shot menampilkan seluruh dapur dan peralatan membuat saus.', 'Tunjukkan senyuman dan ekspresi positif', 3, '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a05a70b7-5146-4d0a-a211-9ff2424fb8cf'::uuid, '02d40f41-4ed1-4d1b-abd0-76f8110e6ef3'::uuid, 1, 1, 'Hook', '0-3s', 'MUG CAKE SEDERHANA!', 'Hai guys! [excited tone] Pengen bikin DESSERT CEPAT yang ENAK banget? Yuk, kita bikin OREO MUG CAKE hanya dalam 90 detik!', 'Extreme close-up pada Oreo yang dihancurkan, lalu zoom out menunjukkan mug.', 'Tunjukkan semangat dan energi positif!', 1, '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('85420f71-e5e8-4da2-8c99-22ee8f3fa658'::uuid, '02d40f41-4ed1-4d1b-abd0-76f8110e6ef3'::uuid, 2, 1, 'Hook', '0-3s', 'RASANYA WOW!', 'Dengan hanya 3 bahan, kalian bisa dapatkan dessert yang WOW! [excited tone]', 'Fast-motion footage saat bahan dituang ke mug, dengan efek suara yang ceria.', 'Gunakan musik upbeat untuk meningkatkan mood!', 2, '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('62b6d4a1-c994-46d2-b539-d8c71f8a8d21'::uuid, '02d40f41-4ed1-4d1b-abd0-76f8110e6ef3'::uuid, 3, 1, 'Hook', '0-3s', 'CEPAT DAN MUDAH!', 'Guys, siapa yang mau dessert yang CEPAT dan MUDAH? Makanya tonton sampai habis ya!', 'Medium shot dengan host berpose sambil memegang mug.', 'Senyum lebar dan ajak audiens berinteraksi!', 3, '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c3a0fabf-5fd5-4103-a77c-3120742fb967'::uuid, 'c18b9328-0ecc-48ef-8451-70f12c3574c6'::uuid, 1, 1, 'Hook', '0-3s', 'PILIH PISAU DENGAN BIJAK!', 'Hei, kalian tahu gak sih?! Memilih pisau dapur yang tepat itu sangat penting! [excited tone]', 'Extreme close-up pisau dapur di atas meja, dengan latar belakang dapur yang rapi, slow zoom out.', 'Start with an engaging smile and eye contact.', 1, '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0ebbd0b1-a66c-4cc8-9aa5-7e0325dd0a2a'::uuid, 'c18b9328-0ecc-48ef-8451-70f12c3574c6'::uuid, 2, 1, 'Hook', '0-3s', 'RAHASIA DAPUR CANTIK!', 'Statistik menunjukkan, 80% kesalahan memasak akibat pisau yang salah! [serious tone] Yuk, kita cari yang tepat!', 'Wide shot dapur, memperlihatkan berbagai jenis pisau, dengan efek dramatis.', 'Use a surprised expression to attract attention.', 2, '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('fdbfdc61-aac7-4eac-931e-4c5ab50bf21a'::uuid, 'c18b9328-0ecc-48ef-8451-70f12c3574c6'::uuid, 3, 1, 'Hook', '0-3s', 'KISAH PISAU DAPUR!', 'Dulu, aku asal pilih pisau dan hasilnya berantakan! [personal tone] Yuk, belajar bersama!', 'Medium shot diri sendiri di dapur, bercerita sambil memegang pisau.', 'Incorporate personal anecdotes to build a connection.', 3, '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1142de74-57fd-4fd1-ba6c-8f356291a872'::uuid, 'e4244740-d32f-4a7a-a3e5-cd833a22da47'::uuid, 1, 1, 'Hook', '0-3s', 'Rahasia Nasi Goreng!', 'HALO GUYS! [excited tone] Kalian tau gak sih, apa RAHASIA dari nasi goreng ala RESTORAN? Yuk, kita bongkar!', 'Extreme close-up dari wajah sambil tersenyum dengan latar belakang dapur.', 'Start with an enthusiastic gesture, pointing to the camera.', 1, '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('84353b5c-79be-4faa-bbd8-b1766cf405a8'::uuid, 'e4244740-d32f-4a7a-a3e5-cd833a22da47'::uuid, 2, 1, 'Hook', '0-3s', 'Bukan Nasi Goreng Biasa!', 'Tahu gak sih? [serious tone] 70% dari rasa nasi goreng itu dari BUMBU! Apa aja sih bumbunya?', 'Medium shot yang menunjukkan bahan-bahan bumbu di meja.', 'Use hand to point at the ingredients.', 2, '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('73d95d01-a89a-4b42-9aec-c20376a7fb78'::uuid, 'e4244740-d32f-4a7a-a3e5-cd833a22da47'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman Nasi Goreng!', 'Dulu, saya pernah makan nasi goreng di restoran mahal...dan ini dia RAHASIAnya! [excited tone]', 'Wide shot di dapur, menyiapkan bahan-bahan dengan latar suara memasak.', 'Share a personal experience to connect with viewers.', 3, '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e53ff16a-9239-4348-9dd6-fe490261871e'::uuid, '63990380-f319-4fbc-9671-0bcdda48de0a'::uuid, 1, 1, 'Hook', '0-3s', 'Siap-siap jadi chef aesthetic!', 'Hai guys! Kalian pengen tau CARA PLATING MAKANAN supaya terlihat AESTHETIC untuk konten sosial media? Yuk, simak!', 'Extreme close-up wajah dengan ekspresi bersemangat, lalu zoom out ke meja yang sudah disiapkan.', 'Mulai dengan ekspresi optimis!', 1, '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('82098f2f-975b-443d-80b2-c8a6892b8bf1'::uuid, '63990380-f319-4fbc-9671-0bcdda48de0a'::uuid, 2, 1, 'Hook', '0-3s', 'Rahasia plating makanan cantik!', 'Apakah kalian tahu bahwa plating yang baik dapat MENGGANDUNG NILAI seni yang tinggi? Kalian perlu tahu triknya!', 'Medium shot dari bahan makanan colorful di atas meja, dengan musik upbeat.', 'Gunakan warna dan kontras!', 2, '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1d9627d6-64d2-4366-971c-06eee0acbaed'::uuid, '63990380-f319-4fbc-9671-0bcdda48de0a'::uuid, 3, 1, 'Hook', '0-3s', 'Biar makananmu laku keras!', 'Aku dulu plating makanan sembarangan, tapi setelah belajar, semua jadi lebih MENARIK! Yuk, saya tunjukkan caranya!', 'Close-up foto plating yang buruk dan kemudian beralih ke yang lebih aesthetic.', 'Cerita singkat untuk menarik perhatian!', 3, '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c206d948-8043-4a9c-b5eb-8e9792b2df45'::uuid, 'd76b5366-0a1f-4d59-a9bf-27ac38060b04'::uuid, 1, 1, 'Hook', '0-3s', 'SIAP UNTUK 7 MENIT?', 'Hai semuanya! [excited tone] Mau punya perut six-pack tanpa alat? Ini dia WORKOUT 7-MENIT yang super EFISIEN!', 'Extreme close-up wajah, memasang ekspresi semangat, kemudian zoom out ke full body shot.', 'Start with high energy and a big smile', 1, '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('393e1924-68ce-4f85-83b3-e35871aa7b4a'::uuid, 'd76b5366-0a1f-4d59-a9bf-27ac38060b04'::uuid, 2, 1, 'Hook', '0-3s', 'WOW, CUMA 7 MENIT!', 'Tahukah kamu? [shocking tone] Cuma 7 MENIT setiap hari bisa bikin perut kamu lebih RATA! Siap coba?', 'Wide shot dengan background gym atau ruangan bersih, sorot cahaya natural.', 'Use hand gestures to highlight importance', 2, '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e3e3bb44-2a93-4f72-a5c3-bbc1b597209d'::uuid, 'd76b5366-0a1f-4d59-a9bf-27ac38060b04'::uuid, 3, 1, 'Hook', '0-3s', 'YUK WORKOUT BERSAMA!', 'Aku pernah mengalami sulitnya mencapai six-pack. [personal tone] Tapi dengan 7 MENIT ini, aku berhasil! Yuk kita lakukan bersama!', 'Medium shot dengan sambil mempersiapkan matras, memberi semangat.', 'Engage audience with relatable story', 3, '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('edb857eb-f9bd-47b1-b8ff-02aa2d3c6997'::uuid, '7b7675b9-cbb5-4343-82fe-ca20b9a434ee'::uuid, 1, 1, 'Hook', '0-3s', 'Terjebak di meja kerja?', 'Hai teman-teman! [excited tone] Pernah gak sih merasa STRES dan KERAS di badan saat kerja lama di depan laptop?', 'Extreme close-up wajah dengan ekspresi kelelahan, lalu zoom out untuk menunjukkan meja kerja.', 'Mulai dengan pertanyaan yang relatable', 1, '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('614f6be7-6a90-4782-ac35-cb92a846a531'::uuid, '7b7675b9-cbb5-4343-82fe-ca20b9a434ee'::uuid, 2, 1, 'Hook', '0-3s', 'Fakta mengejutkan!', 'Stats bilang, 65% pekerja kantoran mengalami masalah OTOT dan SENDI! [serious tone] Yuk kita atasi bersama!', 'Medium shot dengan grafik statistik di layar, menampilkan data tentang pekerja kantoran.', 'Gunakan data yang tidak terduga untuk menarik perhatian', 2, '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c679ac0c-7c30-4a52-90a8-d378ded3de26'::uuid, '7b7675b9-cbb5-4343-82fe-ca20b9a434ee'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman pribadi!', 'Aku dulu sering sakit punggung, sampai aku menemukan RAHASIA stretching ini! [excited tone] Kalian harus coba!', 'Medium shot diri sendiri menunjuk ke punggung, kemudian menunjukkan gerakan stretching.', 'Bawa elemen personal untuk menciptakan koneksi', 3, '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('33a29a0f-e460-4a3e-ab03-af7307a9390a'::uuid, '76f5d625-a8b9-411a-a673-ae2e3dc0220b'::uuid, 1, 1, 'Hook', '0-3s', 'Siap membakar kalori?', 'HAI GUYS! [excited tone] Mau bakar kalori dengan cepat? Yuk, coba 5 gerakan HIIT ini!', 'Extreme close-up wajah dengan senyum lebar, latar belakang gym.', 'Tampilkan semangat dan antusiasme di awal.', 1, '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('510d6e40-8f4f-45e2-97db-09cadb063941'::uuid, '76f5d625-a8b9-411a-a673-ae2e3dc0220b'::uuid, 2, 1, 'Hook', '0-3s', 'Bakar 500 kalori dalam 20 menit?', 'Ternyata, kamu bisa BAKAR 500 kalori hanya dalam 20 menit lho! [surprised tone] Gimana caranya? Tonton sampai selesai!', 'Medium shot menunjukkan gerakan santai sambil mengetik di ponsel.', 'Berikan informasi mengejutkan yang menarik perhatian.', 2, '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('142a4b1a-aefd-4e58-a70b-1871ac8178b6'::uuid, '76f5d625-a8b9-411a-a673-ae2e3dc0220b'::uuid, 3, 1, 'Hook', '0-3s', 'Gerakan yang mudah!', 'Aku pernah bosan dengan workout yang itu-itu aja. [nostalgic tone] Tapi dengan HIIT, workout jadi seru dan efisien!', 'Wide shot menunjukkan background outdoor, berolahraga dengan teman-teman.', 'Gunakan pengalaman pribadi untuk membangun koneksi.', 3, '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('889f7d09-a068-4f77-b73b-01351550009a'::uuid, 'b2f59a20-2b30-44f4-91e4-be18b2781ecc'::uuid, 1, 1, 'Hook', '0-3s', 'DUDUK LAMA? PERHATIKAN INI!', 'Hai semuanya! [excited tone] Kalian sering duduk lama? Yuk, simak cara menjaga POSTUR TUBUH yang benar!', 'Extreme close-up wajah dengan ekspresi penuh perhatian, lalu zoom out ke medium shot saat duduk di meja.', 'Arahkan pandangan langsung ke kamera untuk menarik perhatian.', 1, '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('3d8fb56d-0d96-4719-8322-81609aacd36a'::uuid, 'b2f59a20-2b30-44f4-91e4-be18b2781ecc'::uuid, 2, 1, 'Hook', '0-3s', 'APA YANG TERJADI PADA TUBUH KALIAN?', 'Tahukah kalian? [shocking tone] Duduk lebih dari 8 jam sehari bisa bikin postur tubuh kalian buruk! Ayo perbaiki!', 'Wide shot dengan animasi grafik postur tubuh yang salah dan benar.', 'Gunakan grafik untuk visualisasi dampak negatif dari postur buruk.', 2, '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cd96196c-21fd-46b5-95b0-8818e63c2084'::uuid, 'b2f59a20-2b30-44f4-91e4-be18b2781ecc'::uuid, 3, 1, 'Hook', '0-3s', 'DULU SAYA JUGA BEGITU!', 'Dulu saya juga tidak peduli dengan postur saat duduk. [personal tone] Tapi setelah mengalami nyeri punggung, saya belajar cara yang benar!', 'Medium shot dengan tampilan wajah serius, menekankan pengalaman pribadi.', 'Gunakan ekspresi wajah untuk menunjukkan emosional.', 3, '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('802802bf-0139-4795-a1de-5635fab1bc27'::uuid, 'ae76d49e-e767-4ba5-835c-0275f51a141b'::uuid, 1, 1, 'Hook', '0-3s', 'Siap Latihan di Rumah?', 'Hai guys! [excited tone] Mau tau bagaimana cara latihan dengan RESISTANCE BAND? Yuk, kita coba bareng!', 'Extreme close-up wajah dengan ekspresi bersemangat, zoom out ke medium shot dengan resistance band di tangan...', 'Start with a friendly smile to engage the audience', 1, '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0c99ef1a-3850-4a02-ae08-d7c21ff3f827'::uuid, 'ae76d49e-e767-4ba5-835c-0275f51a141b'::uuid, 2, 1, 'Hook', '0-3s', 'Latihan Mudah dan Efektif!', 'Tahukah kamu? [surprised tone] Latihan dengan resistance band bisa membakar kalori lebih banyak lho! Di mana aja!', 'Wide shot di ruang tamu yang nyaman, band tergantung di rak...kembali ke medium shot.', 'Use engaging facial expressions for emphasis', 2, '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('77b9d4b3-d81c-47ec-8372-e5c3af0c07f3'::uuid, 'ae76d49e-e767-4ba5-835c-0275f51a141b'::uuid, 3, 1, 'Hook', '0-3s', 'Kita Latihan Bareng Yuk!', 'Aku dulu bingung banget, bisa gak ya latihan di rumah? [personal tone] Ternyata mudah banget dengan RESISTANCE BAND!', 'Medium shot dari samping, menggenggam band sambil bercerita, sedikit bergerak.', 'Share a relatable personal experience', 3, '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6201554a-f009-48e6-b146-0d37a3b387cb'::uuid, 'a1f88c38-3111-460b-926a-f40eceecc15a'::uuid, 1, 1, 'Hook', '0-3s', 'SIAP UNTUK TANTANGAN?', 'Hei kalian! [excited tone] Siap untuk tantangan PUSH-UP 30 HARI yang akan bikin kalian lebih FIT?', 'Extreme close-up senyum ceria lalu cepat zoom out ke medium shot, dengan latar belakang gym atau taman.', 'Start with high energy and engaging smile', 1, '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('f4f32226-0517-4028-a0de-e5a42b8cb825'::uuid, 'a1f88c38-3111-460b-926a-f40eceecc15a'::uuid, 2, 1, 'Hook', '0-3s', 'HANYA 30 HARI!', 'Did you know? [shocking tone] Dengan hanya 30 HARI PUSH-UP, kalian bisa mengubah bentuk tubuh kalian! Gak percaya? Yuk buktikan!', 'Medium shot dengan background statistik kebugaran, tampak grafik sebelum dan sesudah.', 'Use hand gestures to highlight points', 2, '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('8952ce76-a280-4c37-9a17-8c20e2d3f4d7'::uuid, 'a1f88c38-3111-460b-926a-f40eceecc15a'::uuid, 3, 1, 'Hook', '0-3s', 'KISAHKU!', 'Dulu aku juga ragu! [personal tone] Tapi setelah 30 hari push-up, aku merasakan perubahan yang luar biasa! Mau tau caranya?', 'Wide shot dengan background transformasi tubuh, kemudian close-up wajah bersemangat.', 'Share personal excitement through facial expressions', 3, '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('3c7aaf92-e913-442c-8630-3d3c9857df7d'::uuid, '87694d20-0367-483f-8fda-8a36fc92bd80'::uuid, 1, 1, 'Hook', '0-3s', 'SEHAT & ENAK!', 'HAI GUYS! [excited] Penasaran dengan apa yang aku makan dalam sehari? Ini dia DIET SEIMBANG yang enak dan bergizi!', 'Extreme close-up wajah excited, kemudian zoom out untuk menunjukkan sarapan.', 'Start with enthusiasm to grab attention.', 1, '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('255c2ecb-1086-46e4-95bd-2ecc032edf0e'::uuid, '87694d20-0367-483f-8fda-8a36fc92bd80'::uuid, 2, 1, 'Hook', '0-3s', 'RAHASIA ENERGI TINGGI!', 'Tahukah kalian? [dramatic pause] Makanan seimbang bisa bikin energi kalian meningkat drastis!', 'Wide shot dengan berbagai makanan sehat di meja, focus ke makanan.', 'Use a surprising statement to engage viewers.', 2, '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('3d923875-31b9-4498-91b6-aafff28027d3'::uuid, '87694d20-0367-483f-8fda-8a36fc92bd80'::uuid, 3, 1, 'Hook', '0-3s', 'SIMPLE & MUDAH!', 'Aku dulu sering bingung... [nostalgic tone] Mau diet tapi tetap pengen makan enak. Nah, sekarang aku punya solusinya!', 'Medium shot menunjukkan presenter dengan makanan di tangan.', 'Share a personal experience to connect with the audience.', 3, '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('46a88e19-59e5-4707-9761-80f5bd326139'::uuid, '0d75aaf9-f506-44e9-8e84-483905b1d5f9'::uuid, 1, 1, 'Hook', '0-3s', 'Cukup Minum Air?', 'Hai guys! [excited tone] Kalian tahu nggak sih, bahwa MENJAGA HIDRASI itu SUPER penting? Yuk, kita bahas!', 'Extreme close-up wajah dengan senyum lebar, soft lighting dari ring light, lalu zoom out ke medium shot kamu memegang botol air.', 'Start with high energy, show the water bottle.', 1, '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('687a1078-3039-43a0-90f1-3809d4b1a1d0'::uuid, '0d75aaf9-f506-44e9-8e84-483905b1d5f9'::uuid, 2, 1, 'Hook', '0-3s', 'KENAPA HARUS?', 'Eh, tahu nggak? Sekitar 60% tubuh kita itu AIR! [serious tone] Bayangkan kalau kita dehidrasi...', 'Medium shot dengan animasi grafik air hilang dari tubuh, menyoroti pentingnya air.', 'Use gestures to emphasize the percentage.', 2, '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('add715ce-17f5-4a34-865f-1b95ffc4aed9'::uuid, '0d75aaf9-f506-44e9-8e84-483905b1d5f9'::uuid, 3, 1, 'Hook', '0-3s', 'TIP MENARIK!', 'Pernah merasa lelah? Itu bisa jadi tanda kalian kurang minum air, guys! [concerned tone]', 'Wide shot dengan kamu duduk lesu, lalu segelas air muncul di tangan.', 'Express relatable experiences.', 3, '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('10e0f3f3-7333-4fe8-9353-a394c2c34586'::uuid, '6020ff28-3774-40a6-904b-bdc0c225c1d3'::uuid, 1, 1, 'Hook', '0-3s', 'MANFAAT WALK-MEETING!', 'Kalian tau gak sih, kalau walk-meeting 15 menit itu bisa ngubah segalanya? [excited]', 'Extreme close-up wajah yang bersemangat, lalu cepat zoom out ke medium shot saat bergerak.', 'Mulai dengan ekspresi antusias', 1, '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c58a5f17-add6-4212-892e-e53ad637c5f5'::uuid, '6020ff28-3774-40a6-904b-bdc0c225c1d3'::uuid, 2, 1, 'Hook', '0-3s', 'SEHAT DAN PRODUKTIF!', 'Fakta menarik! Riset menunjukkan walk-meeting bisa ningkatin mood dan kreativitas. [excited]', 'Medium shot dari orang-orang yang berjalan di taman, senyum sambil berbicara.', 'Gunakan lingkungan yang segar sebagai latar belakang', 2, '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d856cdbd-308c-4c9e-8e80-597c45fc13b4'::uuid, '6020ff28-3774-40a6-904b-bdc0c225c1d3'::uuid, 3, 1, 'Hook', '0-3s', 'CARA ASYIK MEETING!', 'Dulu saya gak percaya, tapi setelah coba walk-meeting 15 menit, semua jadi lebih fokus! [happy]', 'Medium shot momen pertemuan sambil berjalan, orang berbagi ide.', 'Tampilkan pengalaman pribadi yang relatable', 3, '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6643c420-524a-4817-b767-d5979aaef91c'::uuid, '9be732c8-4ffa-44d7-aec8-e2b72e187e2e'::uuid, 1, 1, 'Hook', '0-3s', 'MEDITASI 5 MENIT?', 'Hai guys! [excited tone] Siapa disini yang mau belajar MEDITASI tapi bingung mulai dari mana?', 'Extreme close-up wajah dengan ekspresi antusias, slow zoom out ke medium shot menunjukkan lingkungan yang tenang.', 'Mulai dengan ekspresi ramah dan tatap kamera.', 1, '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0f3b0658-c5e0-41f9-8609-7f35af24a170'::uuid, '9be732c8-4ffa-44d7-aec8-e2b72e187e2e'::uuid, 2, 1, 'Hook', '0-3s', 'HANYA 5 MENIT!', 'Tahukah kalian bahwa hanya dengan 5 MENIT meditasi bisa membuat kalian lebih fokus dan tenang? [informative tone]', 'Medium shot menarik perhatian selama 1-2 detik sebelum beralih ke tips.', 'Gunakan jari telunjuk untuk menekankan ''5 MENIT''.', 2, '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e7abfe10-0c59-4416-8635-fc585e547390'::uuid, '9be732c8-4ffa-44d7-aec8-e2b72e187e2e'::uuid, 3, 1, 'Hook', '0-3s', 'YUK MEDITASI!', 'Dulu aku juga bingung, tapi sekarang meditasi 5 MENIT jadi rutinitas harian aku! [personal tone]', 'Medium shot dengan background tenang sambil tersenyum, mungkin dengan bantal meditasi.', 'Buat gestur mengundang untuk menarik perhatian.', 3, '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('88e47f3a-c895-4fff-af8d-c7d2769f6b98'::uuid, 'bb8648d8-a0ee-4e46-873e-90b5b38bb6b3'::uuid, 1, 1, 'Hook', '0-3s', 'SMARTPHONE BARU!', 'Hai guys! [excited tone] Kalian udah denger tentang smartphone flagship terbaru ini?', 'Extreme close-up wajah excited, zoom out memperlihatkan smartphone di tangan.', 'Engage with a big smile and eye contact', 1, '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('dc83a278-48b4-4850-b69c-b52318708f0d'::uuid, 'bb8648d8-a0ee-4e46-873e-90b5b38bb6b3'::uuid, 2, 1, 'Hook', '0-3s', 'Fitur GILA!', 'Denger-denger, flagship baru ini punya fitur GILA yang harus kalian tau! [curious tone]', 'Wide shot dengan smartphone di meja, fokus ke layar yang menampilkan spesifikasi.', 'Use a surprised expression to create intrigue', 2, '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('06520ffc-0870-4055-a18c-eebb772dc9f3'::uuid, 'bb8648d8-a0ee-4e46-873e-90b5b38bb6b3'::uuid, 3, 1, 'Hook', '0-3s', 'Wajib Tahu!', 'Waktunya kita bahas smartphone flagship terbaru yang bikin heboh! [excited tone]', 'Medium shot dengan tangan memegang smartphone, berjalan ke arah kamera.', 'Hold the smartphone confidently while speaking', 3, '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('8bafc37b-daef-4a84-a5ac-2f3ab99413be'::uuid, 'd3264700-2a3c-43a1-85ea-e3031de81903'::uuid, 1, 1, 'Hook', '0-3s', 'PENTING!', 'HAI GUYS! [excited tone] Apakah kalian tahu, merawat baterai laptop itu bisa BIKIN LAMA TAHAN?', 'Extreme close-up wajah dengan ekspresi antusias, kemudian zoom out ke medium shot menunjukkan laptop.', 'Capture attention with an excited expression.', 1, '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ab15196a-f60e-413e-afaa-3927dab5a008'::uuid, 'd3264700-2a3c-43a1-85ea-e3031de81903'::uuid, 2, 1, 'Hook', '0-3s', 'Fakta Menarik!', 'Ternyata, BATERAI laptop bisa bertahan lebih lama jika dirawat dengan benar. Yuk, simak tipsnya!', 'Medium shot dengan backdrop laptop yang menyala, slow pan ke laptop saat membahas.', 'Provide a surprising fact to engage viewers.', 2, '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('28c9fc2d-d769-46ed-a061-1aafbbd8f2a2'::uuid, 'd3264700-2a3c-43a1-85ea-e3031de81903'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman Pribadi!', 'Dulu, baterai laptop aku cepet habis. Tapi setelah ikutin tips ini, jadi jauh lebih awet! [excited]', 'Close-up wajah dengan ekspresi percaya diri, lalu beralih ke laptop yang sedang diisi daya.', 'Share a personal story to create relatability.', 3, '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('25beac36-795f-4ad8-821d-b8f3bc44e15b'::uuid, 'd19e09e7-4a74-4fdc-8bdb-93549be138d4'::uuid, 1, 1, 'Hook', '0-3s', 'SIAP-SIAP!', 'Halo guys! [excited tone] Kalian harus tahu, ada 3 AI tool GRATIS yang BISA NGEHEMAT waktu dan tenaga kalian!', 'Extreme close-up wajah sambil senyum, lalu zoom out ke medium shot sambil menunjukkan jari telunjuk.', 'Start with high energy and a big smile', 1, '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7350b373-bcd7-4d02-9243-a2294de6dafc'::uuid, 'd19e09e7-4a74-4fdc-8bdb-93549be138d4'::uuid, 2, 1, 'Hook', '0-3s', 'Fakta MENARIK!', 'Tahukah kalian, 60% orang merasa produktivitas meningkat berkat AI? [serious tone] Yuk, kita lihat 3 AI tool GRATIS yang WAJIB kalian coba!', 'Wide shot dengan grafik menarik muncul di layar tentang statistik AI.', 'Use a serious tone to add credibility', 2, '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('036ec15d-7dc5-4bac-979d-939815d75e84'::uuid, 'd19e09e7-4a74-4fdc-8bdb-93549be138d4'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman KU!', 'Hey! [friendly tone] Dulu aku sering kehabisan ide. Tapi setelah pakai 3 AI tool GRATIS ini, semua jadi lebih mudah!', 'Medium shot dengan ekspresi penasaran, menunjukkan tangan di dagu.', 'Connect personally with the audience', 3, '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bf4bccbf-e7f6-4080-8b93-115060b2df24'::uuid, 'efade350-2301-45b5-ba6c-ebd43d641154'::uuid, 1, 1, 'Hook', '0-3s', 'BUAT VIDEO SINEMATIK!', 'Hai guys! [excited] Kalian pengen tau CARA setting kamera smartphone untuk bikin video yang SINEMATIK? Yuk, simak!', 'Extreme close-up wajah dengan ekspresi antusias, light ring untuk pencahayaan yang baik.', 'Senyum dan tatap kamera untuk menarik perhatian', 1, '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('022b3bdb-665f-49f4-a422-0bce4505d390'::uuid, 'efade350-2301-45b5-ba6c-ebd43d641154'::uuid, 2, 1, 'Hook', '0-3s', 'RAHASIA KAMERA!', 'Fakta menarik! [shocking tone] Kebanyakan dari kita belum memanfaatkan fitur kamera smartphone dengan OPTIMAL! Ini dia rahasianya...', 'Medium shot, menatap langsung ke kamera sambil memegang smartphone.', 'Pakai gesture tangan untuk menunjukkan smartphone', 2, '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('2758442d-17e1-4444-b2dc-faecc3656214'::uuid, 'efade350-2301-45b5-ba6c-ebd43d641154'::uuid, 3, 1, 'Hook', '0-3s', 'KISAH SAYA!', 'Dulu, saya juga bingung... [personal tone] Tapi ternyata, setting kamera itu gampang banget! Mari saya tunjukkan.', 'Wide shot di lingkungan yang menarik, memberi kesan cerita yang menyenangkan.', 'Gunakan gaya bercerita yang menarik', 3, '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cc0ca4e9-281e-4b6a-97b2-1fb58ff70575'::uuid, '11653dd9-475c-4dd4-8fb5-6615d41c349d'::uuid, 1, 1, 'Hook', '0-3s', 'USB-C atau Lightning?', 'HAI SEMUA! [excited tone] Kalian bingung antara USB-C dan Lightning? Apa sih bedanya?', 'Extreme close-up tangan yang memegang kabel USB-C dan Lightning, slow zoom out ke medium shot...', 'Start with high energy and show both cables', 1, '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d476d46d-72f7-4aca-aa5e-10e22ffa3675'::uuid, '11653dd9-475c-4dd4-8fb5-6615d41c349d'::uuid, 2, 1, 'Hook', '0-3s', 'Fakta Mengejutkan!', 'Tahu nggak sih? [shocking tone] USB-C bisa transfer data lebih cepat lho dibanding Lightning! Simak penjelasannya...', 'Medium shot kabel USB-C dan Lightning dengan efek teks animasi ''WOW!''...', 'Use facial expressions to enhance shock factor', 2, '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1ea3cf1d-4a54-4efc-b347-d91718dd7607'::uuid, '11653dd9-475c-4dd4-8fb5-6615d41c349d'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman Pribadi', 'Jadi, pengalaman pribadi. [storytelling tone] Saat aku ganti ke USB-C, semuanya jadi lebih cepat. Kenapa ya?', 'Wide shot dengan pengguna mengganti kabel, menunjukkan reaksi positif...', 'Share relatable experiences to connect with audience', 3, '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('82228418-3118-4bce-9a03-086bc6944db9'::uuid, 'bce52fac-f6e0-49ec-8fba-5912239f0602'::uuid, 1, 1, 'Hook', '0-3s', 'MELEDAK TEKNOLOGI!', 'Hai guys! [excited tone] Siapa di sini mau tau bagaimana CARA CEPAT mengetik pakai shortcut di Windows 11?!', 'Extreme close-up wajah dengan ekspresi antusias, zoom out ke medium shot sambil menunjukkan keyboard.', 'Start with a bright smile to grab attention.', 1, '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e3c0b492-a1f2-4c6a-807a-033ef613d8d1'::uuid, 'bce52fac-f6e0-49ec-8fba-5912239f0602'::uuid, 2, 1, 'Hook', '0-3s', 'CEPAT & EFEKTIF!', 'Did you tahu? [serious tone] Menggunakan shortcut bisa meningkatkan produktivitas kalian sampai 50%! Yuk kita pelajari!', 'Medium shot dengan grafik animasi di latar belakang menunjukkan peningkatan produktivitas.', 'Use a strong statistic to emphasize the importance.', 2, '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('eafd207c-337b-4867-8b98-0071ed65b1ac'::uuid, 'bce52fac-f6e0-49ec-8fba-5912239f0602'::uuid, 3, 1, 'Hook', '0-3s', 'PENGALAMAN SAYA!', 'Aku dulu juga lambat banget mengetik... [personal tone] Tapi setelah belajar shortcut ini, semuanya jadi lebih mudah!', 'Medium shot dengan pose santai di meja kerja, menunjukkan tampilan layar laptop.', 'Create a relatable backstory to connect with viewers.', 3, '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9dcba7d1-0307-4256-9d0a-3513f6f31cdb'::uuid, '62c77009-1b98-4205-a2fe-ed07e50989d1'::uuid, 1, 1, 'Hook', '0-3s', 'UNBOXING BAHAYANG!', 'Hey guys! [excited tone] Siapa yang suka musik? Hari ini kita bakal UNBOXING earbuds ANC yang katanya JUARA...', 'Extreme close-up wajah dengan senyuman, memegang kotak earbuds, ring light menyinari dari depan.', 'Start with high energy and eye contact', 1, '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4b7736af-aa5c-4cb6-98fe-9f6369258b89'::uuid, '62c77009-1b98-4205-a2fe-ed07e50989d1'::uuid, 2, 1, 'Hook', '0-3s', 'BAIK ATAU TIDAK?', 'Dengar sini! [serious tone] Apakah earbuds ANC ini benar-benar SEHAT bagi telinga kita? Mari kita lihat...', 'Medium shot memegang earbuds dengan ekspresi penasaran, latar belakang yang cerah.', 'Use hand gestures for excitement', 2, '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('84b80b72-21dc-4900-af88-3706c6113414'::uuid, '62c77009-1b98-4205-a2fe-ed07e50989d1'::uuid, 3, 1, 'Hook', '0-3s', 'PERTAMA KALI!', 'Hai semuanya! [casual tone] Ini pertama kalinya aku coba earbuds ANC ini, jadi BARENGAN ya!', 'Wide shot duduk di meja dengan semua peralatan unboxing, ring light menyinari area.', 'Include a friendly smile', 3, '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('3b73afb5-a2c2-4627-9c32-c893688f6b39'::uuid, 'ba73159c-804c-4da2-9190-82b186364480'::uuid, 1, 1, 'Hook', '0-3s', 'BISAKAH KALIAN?!', 'HAI, guys! [excited tone] Pernah denger tentang WIRELESS CHARGING? Kenapa bisa ngecas tanpa kabel? Yuk, kita bahas!', 'Extreme close-up wajah dengan senyuman, background tampak bersih dan rapi.', 'Jaga ekspresi wajah tetap excited', 1, '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c1a30e15-a6c6-408e-bf86-298818c0d033'::uuid, 'ba73159c-804c-4da2-9190-82b186364480'::uuid, 2, 1, 'Hook', '0-3s', 'FAKTA MENARIK!', 'Tahukah kamu? [serious tone] Wireless charging bisa membuat hidupmu lebih praktis dan cepat! Mari kita lihat cara kerjanya.', 'Medium shot, dengan tools charging seperti charger dan smartphone di meja.', 'Tunjukkan alat-alat dengan jelas', 2, '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c5613d97-9510-4b44-b979-5be5c6de2781'::uuid, 'ba73159c-804c-4da2-9190-82b186364480'::uuid, 3, 1, 'Hook', '0-3s', 'PENGALAMAN PRIBADI!', 'Dulu, aku juga bingung bagaimana cara wireless charging itu, guys! [nostalgic tone] Sekarang, aku mau berbagi penjelasannya.', 'Medium shot, menunjukkan ponsel dan charger wireless sambil senyum.', 'Gunakan bahasa tubuh yang terbuka', 3, '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('509527aa-0c75-4750-8fdb-7472e4024001'::uuid, 'bd9963e3-b98d-45d8-ada3-b1d1c096dddb'::uuid, 1, 1, 'Hook', '0-3s', 'APAKAH KAMU TAHU?', 'HAI TEMAN-TEMAN! [excited tone] Kalian mencari aplikasi catatan terbaik di Android? Well, aku punya 3 rekomendasi...', 'Extreme close-up wajah bersemangat, ring light menyinari wajah, zoom out perlahan untuk menunjukkan background yang bersih.', 'Start with a big smile to engage viewers.', 1, '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('2e5ca229-e56e-493a-ab11-6ca22c1fc729'::uuid, 'bd9963e3-b98d-45d8-ada3-b1d1c096dddb'::uuid, 2, 1, 'Hook', '0-3s', 'RAHASIA KERJA PRODUKTIF!', 'Tahukah kalian, 70% orang merasa lebih produktif dengan catatan digital! Yuk, kita lihat 3 aplikasi terbaiknya!', 'Medium shot memperlihatkan smartphone di tangan sambil menunjukkan layar dengan aplikasi catatan.', 'Use a confident voice to convey authority.', 2, '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4ae27d20-872a-4b0e-80a1-481a4ac0139c'::uuid, 'bd9963e3-b98d-45d8-ada3-b1d1c096dddb'::uuid, 3, 1, 'Hook', '0-3s', 'PENGALAMAN PRIBADI!', 'Jadi, aku pernah kesulitan mengatur catatan. Sampai akhirnya aku menemukan 3 aplikasi ini yang mengubah segalanya!', 'Wide shot di meja belajar, menunjuk smartphone dan laptop yang menampilkan aplikasi.', 'Share a personal touch to build connection.', 3, '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('73f30c86-d958-4bac-8365-bd3d0b3fab5d'::uuid, '657c5234-1077-4849-ac4a-8e8b9475dfe3'::uuid, 1, 1, 'Hook', '0-3s', 'PERHATIAN!', 'GENGS! Kalian SANGAT perlu tau bagaimana caranya BACKUP DATA ke CLOUD secara otomatis!', 'Extreme close-up wajah excited, dengan efek transisi cepat ke medium shot memegang smartphone...', 'Use an exciting tone and facial expressions.', 1, '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1356d4d7-ba29-4651-b2f1-f7caea7d5954'::uuid, '657c5234-1077-4849-ac4a-8e8b9475dfe3'::uuid, 2, 1, 'Hook', '0-3s', 'DATA HILANG?!', 'Tahukah kalian, 60% orang kehilangan data mereka setiap tahun? Jangan jadi salah satunya!', 'Fast zoom out untuk menunjukkan reaksi khawatir sambil memegang laptop...', 'Express urgency with body language.', 2, '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c28b9263-014f-445e-b59c-8c3955ba5e53'::uuid, '657c5234-1077-4849-ac4a-8e8b9475dfe3'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman Pribadi!', 'Aku pernah kehilangan semua foto berharga! Jangan biarkan itu terjadi padamu! Yuk backup data ke cloud!', 'Medium shot dengan gambar foto-foto di sekitar, menunjukkan emosi kehilangan...', 'Connect on a personal level to build trust.', 3, '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b0003661-0f42-4b03-8bde-e7bbd0c4abe2'::uuid, 'e9e086c9-d0f1-4806-8f0e-9954f4d68d27'::uuid, 1, 1, 'Hook', '0-3s', 'BINGUNG MENABUNG?', 'Hai guys! [excited tone] Kalian fresh graduate dan bingung mengatur keuangan? Yuk, kenalan sama aturan 50-30-20!', 'Extreme close-up wajah ceria, slow zoom out ke medium shot dengan latar belakang meja kerja.', 'Start with high energy and relatable expression', 1, '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('541a5e3b-1a84-4288-b99a-d3bbebb9f17d'::uuid, 'e9e086c9-d0f1-4806-8f0e-9954f4d68d27'::uuid, 2, 1, 'Hook', '0-3s', 'RAHASIA KEUANGAN!', 'Tahukah kalian? [shocking tone] Hanya dengan 50-30-20, kalian bisa mengatur uang dengan mudah!', 'Medium shot dengan grafik sederhana di layar tentang 50-30-20.', 'Use visual aids to represent concepts clearly', 2, '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b4053e88-79fe-48dc-b524-255313f17ab2'::uuid, 'e9e086c9-d0f1-4806-8f0e-9954f4d68d27'::uuid, 3, 1, 'Hook', '0-3s', 'DARI PENGALAMAN!', 'Cerita dikit ya! [personal tone] Dulu aku bingung, sekarang aku pakai aturan 50-30-20 dan hasilnya luar biasa!', 'Medium shot dengan ekspresi serius di wajah, latar belakang tempat belajar.', 'Share a personal experience to connect with the audience', 3, '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('f1aa311b-1209-419c-bc44-8b40e1a1aebe'::uuid, '6785cc33-38da-4aef-b0d3-7892d16368fb'::uuid, 1, 1, 'Hook', '0-3s', 'Saham vs Reksa Dana?', 'Kalian tau gak sih? [excited tone] Banyak yang bingung antara SAHAM dan REKSA DANA! Apa bedanya?', 'Extreme close-up wajah dengan ekspresi penasaran, lalu zoom out ke medium shot dengan kertas dan pensil di tangan...', 'Start with a relatable expression', 1, '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b4b00bda-bc7d-466e-81be-994df218d67f'::uuid, '6785cc33-38da-4aef-b0d3-7892d16368fb'::uuid, 2, 1, 'Hook', '0-3s', 'Fakta Menarik!', 'Berdasarkan survei, 60% orang dewasa tidak paham perbedaan antara SAHAM dan REKSA DANA. Yuk kita bahas!', 'Medium shot dengan grafik sederhana di latar belakang, menunjukkan angka survei...', 'Use a confident tone to establish authority', 2, '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cb6e5314-f68d-48ac-9a76-431b8c10c4e7'::uuid, '6785cc33-38da-4aef-b0d3-7892d16368fb'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman Pribadi', 'Dulu aku juga bingung... Kira-kira mana yang lebih baik? [curious tone] Ini dia perbedaannya!', 'Medium shot dengan background yang cozy, memegang kopi sambil merenung...', 'Share a personal anecdote for a connection', 3, '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('57ec72be-88bf-414a-99d9-51cc0947b9c1'::uuid, 'c2d2cd63-e6ad-4ba0-9cbb-007dda8149bb'::uuid, 1, 1, 'Hook', '0-3s', 'PENTING!', 'Hai guys! [excited tone] Kalian pernah bingung mengatur keuangan? [pause] Yuk, kita buat ANGGARAN BULANAN di SPREADSHEET!', 'Extreme close-up pada layar laptop, menunjukkan spreadsheet kosong, kemudian zoom out ke presenter yang tersenyum.', 'Use an enthusiastic voice and relatable expressions.', 1, '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b5e4cb0c-f7fb-4bce-871f-8f25404281b3'::uuid, 'c2d2cd63-e6ad-4ba0-9cbb-007dda8149bb'::uuid, 2, 1, 'Hook', '0-3s', 'ANGGARAN MU SIA-SIA!', 'Tahukah kalian? [serious tone] 60% orang muda gak punya anggaran bulanan. [pause] Jangan jadi salah satunya!', 'Dynamic text animation dengan fakta mengejutkan, lalu beralih ke presenter.', 'Use bold visuals to highlight statistics.', 2, '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c7001c29-c333-46e9-a125-e9d0cd23def2'::uuid, 'c2d2cd63-e6ad-4ba0-9cbb-007dda8149bb'::uuid, 3, 1, 'Hook', '0-3s', 'CARA MUDAH!', 'Dulu, aku juga bingung! [personal tone] Tapi sekarang, aku sudah membuat anggaran bulanan yang bikin hidup lebih mudah. [pause] Ayo, aku ajarin kalian!', 'Presenter menunjukkan ekspresi bingung di awal, lalu beralih ke kurang lebih bahagia.', 'Share a relatable story to connect with the audience.', 3, '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b35b71a3-b1fb-4626-8628-89f77071cb48'::uuid, '7166f4f6-cef1-4061-9f75-d2c6e97cd09e'::uuid, 1, 1, 'Hook', '0-3s', 'SIAP UNTUK DARURAT?', 'Hai guys! [excited tone] Kalian tahu gak sih, EMERGENCY FUND itu penting banget buat masa depan kita?!', 'Extreme close-up wajah dengan ekspresi antusias, background minimalis.', 'Start with an exciting tone to grab attention.', 1, '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('106d85a5-7944-4602-99ea-331926b37640'::uuid, '7166f4f6-cef1-4061-9f75-d2c6e97cd09e'::uuid, 2, 1, 'Hook', '0-3s', 'Tahukah kamu?', 'Statistik menunjukkan, 75% orang muda belum punya EMERGENCY FUND! [serious tone] Yuk kita bahas cara memulainya!', 'Wide shot dengan infographic di layar yang menunjukkan statistik.', 'Use visuals to emphasize your point.', 2, '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('3d27abff-701b-4ec1-8395-2f847033466f'::uuid, '7166f4f6-cef1-4061-9f75-d2c6e97cd09e'::uuid, 3, 1, 'Hook', '0-3s', 'Cerita saya...', 'Jadi, waktu itu aku tiba-tiba harus bayar biaya rumah sakit. [serious tone] Untungnya ada EMERGENCY FUND yang nyelamatin aku!', 'Medium shot dengan ekspresi serius, backdrop dengan foto keluarga.', 'Share a relatable personal story.', 3, '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4089d56f-9036-4ac9-bba0-e1be965c794f'::uuid, 'd9d718c8-8a6f-4ea1-b06d-618e90208e42'::uuid, 1, 1, 'Hook', '0-3s', 'RAHASIA BELANJA HEMAT!', 'Hai! [excited tone] Kalian suka belanja online? Yuk, kita bahas CARA HEMAT dengan aplikasi CASHBACK!', 'Extreme close-up wajah, senyuman lebar, lalu zoom out ke medium shot dengan handphone di tangan.', 'Energi positif dan senyum lebar', 1, '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('52e22670-0f97-464d-b8ea-3fcbfb782190'::uuid, 'd9d718c8-8a6f-4ea1-b06d-618e90208e42'::uuid, 2, 1, 'Hook', '0-3s', 'DID YOU KNOW?', 'Tahukah kalian bahwa... [shocking tone] Kamu bisa dapatkan hingga 50% kembali dari belanja online mu? Yuk, simak caranya!', 'Medium shot dengan grafik cashback yang muncul di layar.', 'Tampilkan angka/visual yang menarik', 2, '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('87f47ab2-8448-46eb-b4b9-55fc53fac6ba'::uuid, 'd9d718c8-8a6f-4ea1-b06d-618e90208e42'::uuid, 3, 1, 'Hook', '0-3s', 'PENGALAMAN PRIBADI!', 'Jadi, waktu itu aku belanja online... [excited tone] dengan aplikasi cashback ini, aku hemat RATUSAN RIBU! Mau tahu caranya?', 'Medium shot dengan props belanjaan dan handphone di tangan.', 'Gunakan gestur tangan untuk menunjukkan antusiasme', 3, '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9339d564-7327-4575-b826-a1b39b1767cd'::uuid, 'c1ecdfdd-fa39-4767-9864-7b23d51f98b6'::uuid, 1, 1, 'Hook', '0-3s', 'Siapa yang pernah salah kelola uang?', 'Hai guys! [excited tone] Kalian tau gak sih? Banyak anak muda yang punya KESALAHAN FINANSIAL di usia 20-an...', 'Extreme close-up wajah dengan ekspresi kaget, fokus ke mata...', 'Mulai dengan ekspresi wajah yang menarik perhatian', 1, '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c6301eeb-b7fe-48c7-843a-1541ab2369ab'::uuid, 'c1ecdfdd-fa39-4767-9864-7b23d51f98b6'::uuid, 2, 1, 'Hook', '0-3s', 'Statistik mengejutkan!', 'Dengar ini! [serious tone] 70% anak muda mengalami KESALAHAN KEUANGAN ketika berusia 20-an...', 'Visual grafik di belakang yang menunjukkan statistik, medium shot...', 'Gunakan grafik menarik untuk menarik perhatian', 2, '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9f52da69-6b88-4017-b4b4-2ac3905448bf'::uuid, 'c1ecdfdd-fa39-4767-9864-7b23d51f98b6'::uuid, 3, 1, 'Hook', '0-3s', 'Kisahku, pelajaranku!', 'Gue pernah ngalamin sendiri! [nostalgic tone] Kesalahan finansial yang bikin gue pusing di awal 20-an...', 'Medium shot kepala menunduk, dengan transisi ke wajah yang lebih optimis...', 'Berbagi pengalaman pribadi dapat membangun koneksi', 3, '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('01ba303a-73c7-430e-a574-dc3d68a76885'::uuid, 'ca27451b-a8ba-46e2-8bba-e75b75430b5f'::uuid, 1, 1, 'Hook', '0-3s', 'CARA AMAN INVESTASI EMAS!', 'Hai, guys! [excited tone] Mau tau CARA AMAN INVESTASI EMAS DIGITAL? Ini dia rahasianya!', 'Extreme close-up wajah dengan ekspresi antusias, latar belakang cerah, slow zoom out...', 'Tunjukkan ekspresi wajah yang percaya diri', 1, '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('27233ccf-596f-4fb8-8ee3-46a39adc28dc'::uuid, 'ca27451b-a8ba-46e2-8bba-e75b75430b5f'::uuid, 2, 1, 'Hook', '0-3s', 'Statistik Menarik!', 'Tahukah kamu? [serious tone] Investasi emas digital meningkat 200% dalam satu tahun terakhir! Yuk, kita jelajahi lebih lanjut!', 'Grafik statistik ditampilkan di layar dengan efek visual dinamis...', 'Gunakan gesture tangan untuk menekankan poin', 2, '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a0795a50-6625-473a-a728-3d1a483261c9'::uuid, 'ca27451b-a8ba-46e2-8bba-e75b75430b5f'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman Pribadi!', 'Sebelumnya, aku merasa ragu tentang investasi emas digital. [thoughtful tone] Tapi... sekarang aku tahu CARA AMAN untuk memulainya!', 'Cuplikan tangan yang memegang smartphone, scroll aplikasi investasi...', 'Ciptakan koneksi dengan penonton melalui cerita pribadi', 3, '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('68d1d02e-4daf-485d-ba3d-e6bdb945683e'::uuid, '56ee3216-38e7-4442-b4fb-849d651e96cb'::uuid, 1, 1, 'Hook', '0-3s', 'PENGEN HEMAT?', 'Kalian pernah denger tentang BUDGETING ALA AMPLOP? [excited tone] Ini cara seru mengatur keuangan!', 'Extreme close-up wajah dengan ekspresi antusias, zoom out untuk menunjukkan amplop berwarna-warni.', 'Mulai dengan perkenalan yang menarik.', 1, '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('402aefab-c5c9-4e2d-847e-a5ea66a8e463'::uuid, '56ee3216-38e7-4442-b4fb-849d651e96cb'::uuid, 2, 1, 'Hook', '0-3s', 'RAHASIA UANG KELUAR!', 'Fakta mengejutkan! Banyak orang yang tidak tahu seberapa pentingnya BUDGETING ALA AMPLOP! [serious tone]', 'Medium shot dengan grafik uang dan amplop di latar belakang.', 'Gunakan grafik menarik untuk menunjukkan data.', 2, '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('137f6d8a-fb85-4186-9c9b-f8d14df7bb88'::uuid, '56ee3216-38e7-4442-b4fb-849d651e96cb'::uuid, 3, 1, 'Hook', '0-3s', 'MULAI HEMAT!', 'Aku dulu selalu kehabisan uang! Tapi sekarang...dengan BUDGETING ALA AMPLOP, hidupku jadi lebih teratur! [excited tone]', 'Medium shot menampilkan diri yang terlihat lega dan bahagia sambil menunjukkan amplop.', 'Cerita pengalaman pribadi agar lebih relatable.', 3, '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('58fe9db1-c442-419d-8aa1-67e710d65688'::uuid, '098304a2-a8f2-40fb-8322-fea897f57848'::uuid, 1, 1, 'Hook', '0-3s', 'PENGLIHATAN KAYA!', 'Hai guys! [excited tone] Kamu pernah denger tentang BUNGA MAJOR? Ini bisa bikin uangmu BERTUMBUH cepat!', 'Extreme close-up wajah yang ceria, lalu cepat zoom out ke medium shot.', 'Start with an enthusiastic expression to grab attention.', 1, '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('61ddb0d8-f878-444d-ac3d-39b4b0bb3b38'::uuid, '098304a2-a8f2-40fb-8322-fea897f57848'::uuid, 2, 1, 'Hook', '0-3s', 'Wow, ini dia!', 'Tahukah kamu? [serious tone] Dengan bunga majemuk, uangmu bisa jadi dua kali lipat dalam waktu yang lebih singkat daripada yang kamu pikirkan!', 'Wide shot dengan grafik animasi uang berlipat ganda di sisi.', 'Use a surprising statistic to intrigue viewers.', 2, '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b49bc850-6931-4907-95f3-ad5fb9134fd0'::uuid, '098304a2-a8f2-40fb-8322-fea897f57848'::uuid, 3, 1, 'Hook', '0-3s', 'Pengalaman Pribadi!', 'Dulu aku bingung tentang cara investasi. [conversational tone] Tapi setelah belajar tentang BUNGA MAJEMUK, semuanya jadi jelas!', 'Medium shot memegang buku atau alat tulis dengan animasi latar belakang.', 'Share a personal connection to make it relatable.', 3, '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('73e09f74-5283-46c3-baeb-8e8695409984'::uuid, 'e004d6d6-e2ef-43b0-9508-c0594cacb4b1'::uuid, 1, 1, 'Hook', '0-3s', 'UTANG? GAK PERLU PANIK!', 'Hai guys! [excited tone] Kalian punya utang dan bingung cara bayar? Yuk, cek STRATEGI SNOWBALL ini!', 'Extreme close-up wajah berbinar, dengan ring light menyala cerah. Pelan-pelan zoom out ke medium shot.', 'Start with a relatable emotional expression.', 1, '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('8bf16fd8-8c30-4cd0-9954-c17f6a5fb242'::uuid, 'e004d6d6-e2ef-43b0-9508-c0594cacb4b1'::uuid, 2, 1, 'Hook', '0-3s', 'Fakta MENARIK!', 'Tahukah kalian? [serious tone] 80% orang bisa keluar dari utang dengan metode yang tepat! Yuk, kita bahas!', 'Medium shot dengan grafik menarik tentang utang di background, sedikit zoom in.', 'Use infographics for impactful visuals.', 2, '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', NULL);
        INSERT INTO hook_variants
        (id, training_pair_id, hook_variant, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('41e2bbe1-7da7-4006-819c-4d9feafa922c'::uuid, 'e004d6d6-e2ef-43b0-9508-c0594cacb4b1'::uuid, 3, 1, 'Hook', '0-3s', 'Cerita Pribadi!', 'Dulu, saya juga berjuang dengan utang. [empathetic tone] Tapi, setelah mencoba metode SNOWBALL, hidup saya berubah! Ketahui caranya!', 'Medium shot, posisi duduk santai, menunjukkan ekspresi bersyukur, lighting natural.', 'Make personal stories relatable.', 3, '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', NULL);

               
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('13976eb3-be20-44a7-b674-b7eb3aa92d4f'::uuid, '19bd4e57-f36b-4176-b82a-0a5e5cda024a'::uuid, 2, 'Main Content', '3-8s', 'TIPS #1: RENCANAKAN HARI HARIAN', 'Pertama, kalian harus RENCANAKAN aktivitas kalian! [excited tone] Buat daftar tugas setiap pagi dan prioritas yang penting!', 'Medium shot dengan creator menulis di planner atau catatan. Close-up pada daftar tugas.', 'Show the process of planning with enthusiasm.', 2, '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('89e51bb0-8382-483d-8da5-d072700ca6bd'::uuid, '19bd4e57-f36b-4176-b82a-0a5e5cda024a'::uuid, 3, 'Main Content', '8-14s', 'TIPS #2: HINDARI MULTITASKING', 'Kedua, hindari MULTITASKING! [serious tone] Fokus pada satu tugas, selesaikan, lalu pindah ke yang lain. Kualitas lebih penting dari kuantitas!', 'Medium shot dengan creator menunjukkan dua layar, satu dengan banyak aplikasi terbuka, dan satu lagi hanya satu aplikasi yang sedang digunakan.', 'Demonstrate the difference between multitasking and single-tasking.', 3, '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7dc4c5ed-b5de-4f2f-8b98-0b7355b4438a'::uuid, '19bd4e57-f36b-4176-b82a-0a5e5cda024a'::uuid, 4, 'Main Content', '14-20s', 'TIPS #3: ISTIRAHAT SINGKAT', 'Ketiga, jangan lupa ISTIRAHAT! [encouraging tone] Setiap 25 menit kerja, ambil 5 menit untuk bergerak dan segarkan pikiran!', 'Wide shot menunjukkan creator beristirahat, berdiri, dan melakukan peregangan.', 'Encourage viewers to take breaks using an energetic demonstration.', 4, '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', '2025-07-20 11:02:21.958', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cec1cb59-df8e-47cd-bf7b-c34356851717'::uuid, 'c46e1d12-f30c-4abb-a204-ccd02a0d0c2b'::uuid, 2, 'Main Content', '3-8s', 'DAMPAT #1', 'Pertama, AI MEMPERCEPAT proses belajar! Dengan tutorial video dan materi interaktif, kalian bisa belajar dengan cara yang lebih MENYENANGKAN.', 'Medium shot dengan contoh aplikasi pendidikan di layar, pan ke kanan untuk menunjukkan fitur interaktif...', 'Show visual examples of AI tools', 2, '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('fb7b2035-621d-4138-a4e4-9b5ad205b367'::uuid, 'c46e1d12-f30c-4abb-a204-ccd02a0d0c2b'::uuid, 3, 'Main Content', '8-14s', 'DAMPAT #2', 'Kedua, AI MEMPERSONALISASI pembelajaran! Dengan analisis data, AI bisa memberi saran materi yang sesuai dengan KEBUTUHAN kalian.', 'Medium shot menunjukkan grafik perkembangan belajar di layar, zoom in pada grafik...', 'Highlight personal stories of students', 3, '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('3682c9e9-ea60-44e7-ae6c-41319adbe7d8'::uuid, 'c46e1d12-f30c-4abb-a204-ccd02a0d0c2b'::uuid, 4, 'Main Content', '14-20s', 'DAMPAT #3', 'Ketiga, AI MEMBANTU guru dalam pengajaran! Dengan alat analisis, guru bisa fokus pada cara terbaik untuk mendukung siswa.', 'Medium shot dengan guru menggunakan laptop dan menjelaskan data kepada siswa...', 'Use engaging visuals of teachers at work', 4, '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('daebb357-5295-4f13-9bf2-39b87ab308dd'::uuid, 'c46e1d12-f30c-4abb-a204-ccd02a0d0c2b'::uuid, 5, 'Main Content', '20-25s', 'CALL TO ACTION', 'Jadi, bagaimana menurut kalian? Apakah AI akan mengubah cara kita belajar? TULIS DI KOMENTAR!', 'Close-up wajah talent dengan ekspresi serius, slow zoom in saat mengajak komentar...', 'Encourage audience engagement with a clear question', 5, '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', '2025-07-20 11:04:32.585', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cdc1372a-e67b-4e6c-9e1c-b7ae9f2b7282'::uuid, 'fe57a17a-d5c8-4d02-b57c-b5e41d79dc8f'::uuid, 2, 'Main Content', '3-8s', 'TIP #1: BUAT JADWAL!', 'Pertama, buatlah jadwal harian. [serious tone] Tuliskan tugas-tugas yang harus dikerjakan dan prioritaskan!', 'Medium shot menunjukkan penggunaan aplikasi kalender di ponsel, close-up pada layar.', 'Demonstrate using popular scheduling apps.', 2, '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0721b41a-caac-4e90-b86e-d347c416b187'::uuid, 'fe57a17a-d5c8-4d02-b57c-b5e41d79dc8f'::uuid, 3, 'Main Content', '8-13s', 'TIP #2: ISTIRAHAT YANG CUKUP!', 'Kedua, jangan lupa untuk istirahat. [calm tone] Otak kita perlu recharge setelah belajar keras!', 'Wide shot dengan saya mengambil secangkir kopi dan melihat keluar jendela, tersenyum.', 'Illustrate breaks with relaxing actions.', 3, '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('943f61ad-ebe5-41bf-8d61-927db381f542'::uuid, 'fe57a17a-d5c8-4d02-b57c-b5e41d79dc8f'::uuid, 4, 'Main Content', '13-18s', 'TIP #3: HINDARI DISTRAKSI!', 'Terakhir, matikan notifikasi yang tidak penting. [motivational tone] Fokus itu kunci keberhasilan!', 'Medium shot ponsel dengan notifikasi yang dimatikan, memperlihatkan tampilan tanpa gangguan.', 'Show before and after scenarios for distractions.', 4, '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c4f59269-eb8d-4479-9da3-50f73e75b5d4'::uuid, 'fe57a17a-d5c8-4d02-b57c-b5e41d79dc8f'::uuid, 5, 'Call to Action', '18-25s', 'SEGERA COBA!', 'Coba tips ini sekarang juga! [excited tone] Dan jangan lupa untuk follow untuk lebih banyak tips keren lainnya!', 'Medium shot, senyum lebar, dengan jari menunjuk ke follow button di layar.', 'Use friendly body language to encourage following.', 5, '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', '2025-07-20 13:15:32.782', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cfea1f79-83bb-4843-9a48-5b87f974deac'::uuid, '203268ac-3c9f-4db6-9689-fc4e51818998'::uuid, 2, 'Main Content', '3-8s', 'RAHASIA #1', 'Pertama, BIKIN DAFTAR TUGAS! [excited tone] Dengan mencatat semua yang perlu dilakukan, kamu bisa lebih fokus dan tidak lupa.', 'Medium shot memperlihatkan tangan menulis di kertas, fokus pada tulisan di daftar.', 'Tunjukkan proses penulisan daftar untuk visualisasi yang kuat.', 2, '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6bbddea9-6147-4ac6-94aa-c81c7aa70e53'::uuid, '203268ac-3c9f-4db6-9689-fc4e51818998'::uuid, 3, 'Main Content', '8-13s', 'RAHASIA #2', 'Kedua, ATUR WAKTU! [enthusiastic tone] Gunakan teknik Pomodoro, kerjakan 25 menit, istirahat 5 menit. Gampang, kan?', 'Wide shot menunjukkan timer di meja, dengan pengguna fokus bekerja.', 'Tampilkan timer secara jelas agar penonton bisa mengikutinya.', 3, '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('f0e564e3-81fd-4b4e-8049-83a7118546b4'::uuid, '203268ac-3c9f-4db6-9689-fc4e51818998'::uuid, 4, 'Main Content', '13-20s', 'CATAT PERKEMBANGAN!', 'Terakhir, CATAT progres kalian! [motivational tone] Ini bikin kalian lebih termotivasi dan bersemangat untuk terus maju!', 'Medium shot menunjukkan grafik kemajuan di layar, pengguna tersenyum saat melihat hasil kerja.', 'Tunjukkan kemajuan visual untuk inspirasi dan motivasi.', 4, '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', '2025-07-20 13:16:01.292', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('67caff7a-6255-4257-9688-05ceeab1f8ee'::uuid, '1141bbe1-749c-4081-a55b-8ec509ffef4a'::uuid, 2, 'Main Content', '3-8s', 'TIPS #1: TULIS DI KERTAS!', 'Pertama, guys! TULIS semuanya di kertas. Secara fisik, bisa membantu otak untuk memproses info lebih baik. [excited tone] Ambil catatan dan mulai menulis!', 'Medium shot menunjukkan tangan menulis di kertas, dengan fokus pada detail tulisan.', 'Show the writing process.', 2, '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d576061e-6b0b-48b2-be4b-805ab3da5dd2'::uuid, '1141bbe1-749c-4081-a55b-8ec509ffef4a'::uuid, 3, 'Main Content', '8-13s', 'TIPS #2: PRIORITASKAN!', 'Kedua, PRIORITASKAN tugas kalian! Gunakan sistem bintang atau nomor untuk menentukan mana yang paling penting. [excited tone] Jangan sampai kehabisan waktu untuk yang tak penting!', 'Close-up pada kertas dengan tugas yang ditandai atau diberi bintang.', 'Demonstrate prioritization visually.', 3, '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c9cd1449-6a0d-4b1e-9e2a-2b2ef3166610'::uuid, '1141bbe1-749c-4081-a55b-8ec509ffef4a'::uuid, 4, 'Main Content', '13-18s', 'TIPS #3: TANDAI YANG SUDAH SELESAI!', 'Ketiga, TANDAI tugas yang sudah selesai! Rasanya memuaskan banget, kan? [excited tone] Ini bikin kita semangat untuk menyelesaikan sisanya!', 'Medium shot menunjukkan seseorang mencoret tugas di kertas dengan senyum puas.', 'Show the feeling of accomplishment.', 4, '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e7cae717-0a83-4b10-b822-fce7d4c63b87'::uuid, '1141bbe1-749c-4081-a55b-8ec509ffef4a'::uuid, 5, 'Main Content', '18-23s', 'KLIK LIKE & FOLLOW!', 'Nah, mudah kan? [excited tone] Coba tips ini dan rasakan perbedaannya. Jangan lupa KLIK LIKE dan FOLLOW untuk lebih banyak tips produktivitas!', 'Wide shot presenter dengan senyum, melambai ke arah kamera, lalu menampilkan tombol like dan follow di layar.', 'Encourage interaction with a strong CTA.', 5, '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', '2025-07-20 13:16:34.495', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6fc1c0d7-c297-4fbe-b3e7-91bbb2b5a29f'::uuid, '69b96c49-437f-4d86-ba7f-c1bb35899c93'::uuid, 2, 'Main Content', '3-10s', 'APA ITU POMODORO?', 'Nah, teknik Pomodoro itu simple banget! Kalian belajar selama 25 menit, terus istirahat 5 menit. [excited tone] Keren, kan?', 'Medium shot menunjukkan seseorang menggunakan timer digital untuk memulai sesi belajar.', 'Use an engaging visual demonstration of the timer', 2, '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('5c19b835-e5b5-441d-9286-42a7a32903d5'::uuid, '69b96c49-437f-4d86-ba7f-c1bb35899c93'::uuid, 3, 'Main Content', '10-15s', 'KENAPA EFISIEN?', 'Kenapa teknik ini efisien? Karena fokus kita meningkat setelah istirahat singkat! [informative tone] Bikin kerja otak lebih fresh.', 'Cut to a diagram yang menunjukkan peningkatan fokus selama sesi Pomodoro.', 'Incorporate relatable visuals to keep viewers engaged', 3, '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('29cc06e1-beaf-449c-88e0-c693fd0fe274'::uuid, '69b96c49-437f-4d86-ba7f-c1bb35899c93'::uuid, 4, 'Main Content', '15-20s', 'SIAP COBALAH?', 'Yuk, coba teknik Pomodoro ini! Biar fokus belajar kalian makin oke! [strong upbeat tone] Jangan lupa share hasilnya, ya!', 'Close-up pada wajah yang bersemangat, mengacungkan jempol, dan menunjukkan sesi belajar yang berhasil.', 'Encourage viewers to take action and share their experiences', 4, '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', '2025-07-20 13:17:01.293', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('f6d333eb-21c3-4cc4-b072-27640a55261d'::uuid, '09407675-a975-4315-892a-606cd413f95c'::uuid, 2, 'Main Content', '3-10s', 'TIP #1: RUTINITAS NYATA', 'Pertama, buatlah RUTINITAS yang jelas! Tentukan waktu untuk kerja, istirahat, dan menyusun task. JANGAN sampai campur aduk!', 'Medium shot dengan demonstrasi planner atau aplikasi manajemen tugas, pan dengan lembut untuk menunjukkan jadwal...', 'Show a physical planner or app to illustrate', 2, '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ab7fe007-754b-47be-bc2c-0f0359026ead'::uuid, '09407675-a975-4315-892a-606cd413f95c'::uuid, 3, 'Main Content', '10-17s', 'TIP #2: TEMPAT YANG NYAMAN', 'Kedua, pastikan tempat kerjamu nyaman! Gunakan kursi yang baik, pencahayaan yang cukup, dan dekorasi yang menyenangkan. KENYAMANAN itu KUNCI!', 'Wide shot menunjukkan posisi kursi dan meja, dengan penggunaan tanaman kecil sebagai hiasan...', 'Include visuals of comfort elements', 3, '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('df8ac132-27b1-4461-b4d5-1a4602dc1395'::uuid, '09407675-a975-4315-892a-606cd413f95c'::uuid, 4, 'Main Content', '17-24s', 'TIP #3: MINIMALIS', 'Terakhir, DEKORASI MINIMALIS! Singkirkan barang-barang yang tidak perlu. SEMAKIN SEDIKIT, SEMAKIN FOKUS!', 'Medium shot menunjukkan proses merapikan meja, mengurangi clutter, dengan zoom in pada barang yang sudah disingkirkan...', 'Demonstrate decluttering visually', 4, '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1f703848-45d9-4392-a9e5-2ee57374aad6'::uuid, '09407675-a975-4315-892a-606cd413f95c'::uuid, 5, 'CTA', '24-25s', 'Coba sekarang!', 'Jadi, sudah siap UBAH workspace-mu? Tulis di kolom komentar, ya!', 'Close-up wajah dengan senyum, jari menunjuk ke arah kolom komentar, dan latar belakang yang bersih dan rapi...', 'Encourage interaction with the audience', 5, '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', '2025-07-20 13:17:28.166', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9e5624dc-e153-4abf-b9ae-94478ce4df47'::uuid, '2ccf569a-a37b-475b-a36c-ffe9b06ce393'::uuid, 2, 'Main Content', '3-8s', 'TIP 1: SIAPKAN MALAM SEBELUMNYA', 'Pertama, pastikan kalian SIAPKAN SEMUA SEBELUM TIDUR... [serious tone] Atur alarm, rapikan meja kerja, dan batasi screen time. Kalian pasti lebih mudah bangun!', 'Medium shot menunjukkan persiapan malam, menyiapkan pakaian dan merapikan meja kerja.', 'Demonstrate preparation steps.', 2, '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4fd76757-4441-4d1d-abea-eb73b7d5c36a'::uuid, '2ccf569a-a37b-475b-a36c-ffe9b06ce393'::uuid, 3, 'Main Content', '8-13s', 'TIP 2: RUTINITAS PAGI YANG MENENANGKAN', 'Kedua, buat RUTINITAS PAGI YANG MENENANGKAN... [calm tone] Seperti meditasi atau olahraga ringan. Kalian akan merasa lebih segar dan siap bekerja!', 'Medium shot melakukan yoga atau stretching di luar dengan pemandangan matahari terbit.', 'Highlight the benefits of a morning routine.', 3, '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0036bb56-4e0e-4697-b73c-42296c839dd4'::uuid, '2ccf569a-a37b-475b-a36c-ffe9b06ce393'::uuid, 4, 'Main Content', '13-18s', 'TIP 3: CAIRKAN AIR PUTIH', 'Terakhir, minum AIR PUTIH setelah bangun bisa bantu tubuh kalian JUMLAHKAN ENERGI... [excited tone] Siapkan segelas air di samping tempat tidur, ya!', 'Close-up gelas air di samping tempat tidur, menunjukkan peminuman air setelah bangun.', 'Visually demonstrate the act of drinking water.', 4, '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('745a2cb2-b03f-40be-8b1d-90f89102ab45'::uuid, '2ccf569a-a37b-475b-a36c-ffe9b06ce393'::uuid, 5, 'Call to Action', '18-25s', 'YUK COBALAH!', 'Jadi, apakah kalian siap bangun pagi jam 5 subuh? [excited tone] Coba tips ini dan kasih tau aku hasilnya di komentar! Jangan lupa follow untuk lebih banyak tips!', 'Wide shot dengan senyuman dan jari menunjuk ke arah kamera, latar belakang cerah.', 'Encourage viewer interaction and engagement.', 5, '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', '2025-07-20 13:17:56.612', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('96cc7d77-ed7a-477c-9767-8c2666a33653'::uuid, '12def5a0-1dc7-4f12-a42d-6fa7a1aa6329'::uuid, 2, 'Main Content', '3-8s', 'RAHASIA #1: BANGUN PAGI', 'Kebiasaan pertama, BANGUN PAGI! [excited] Dengan bangun lebih awal, kalian punya WAKTU lebih untuk merencanakan hari, tanpa terburu-buru!', 'Medium shot menunjukkan seseorang bangun dari tempat tidur dengan semangat, lalu mengambil notebook.', 'Tunjukkan rutinitas pagi yang positif.', 2, '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('159978cf-2727-48a2-9423-cf60f0e8dea0'::uuid, '12def5a0-1dc7-4f12-a42d-6fa7a1aa6329'::uuid, 3, 'Main Content', '8-13s', 'RAHASIA #2: BUAT LIST TUGAS', 'Kedua, BUAT LIST TUGAS! [excited] Ini membantu kalian tetap fokus. Cek setiap tugas yang sudah selesai untuk perasaan pencapaian!', 'Close-up menunjukkan tangan menulis di notebook, lalu mencoret tugas yang sudah selesai.', 'Perlihatkan ekspresi puas saat mencoret.', 3, '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6a81f40f-c0d0-4ea2-896e-944ebe22dac9'::uuid, '12def5a0-1dc7-4f12-a42d-6fa7a1aa6329'::uuid, 4, 'Main Content', '13-18s', 'RAHASIA #3: JAGA KONSENTRASI', 'Ketiga, JAGA KONSENTRASI! [serious] Matikan notifikasi yang mengganggu dan gunakan teknik Pomodoro: kerja 25 menit, istirahat 5 menit!', 'Wide shot menunjukkan seseorang bekerja di laptop dengan timer terlihat di layar, mengatur fokus.', 'Peragakan suasana kerja yang tenang dan fokus.', 4, '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b2b75739-d6b4-4a67-9562-5dfef88d0e40'::uuid, '12def5a0-1dc7-4f12-a42d-6fa7a1aa6329'::uuid, 5, 'Call to Action', '18-25s', 'Coba Sekarang!', 'Jadi, ayo coba kebiasaan kecil ini dan rasakan perbedaannya! Share video ini ke teman-teman yang butuh motivasi!', 'Medium shot dengan senyuman lebar, menunjukkan jari menunjuk ke arah kamera.', 'Akhiri dengan energi positif dan senyuman.', 5, '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', '2025-07-20 13:18:34.542', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('f4384b21-2897-4d1a-9f0d-94d1896294a0'::uuid, 'e52583e6-d622-411a-b8f3-c053c487c8f5'::uuid, 2, 'Main Content', '3-8s', 'APA ITU DIGITAL DETOX?', 'Digital detox adalah mematikan gadget untuk 24 jam! [serious tone] Ini membantu kita recharge pikiran dan mengurangi stres.', 'Wide shot dengan props seperti buku dan tanaman, menunjukkan aktivitas tanpa gadget.', 'Show various activities like reading or walking.', 2, '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d805c3c1-66c7-4ce3-878a-416a03d79dd3'::uuid, 'e52583e6-d622-411a-b8f3-c053c487c8f5'::uuid, 3, 'Main Content', '8-13s', 'MANFAATNYA!', 'Manfaatnya? [excited tone] Lebih fokus, lebih produktif, dan tentunya, lebih bahagia! Coba deh, kalian pasti terkejut!', 'Dynamic medium shot dengan ekspresi bahagia dan surga alam di latar belakang.', 'Add quick clips of fun activities.', 3, '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('44c43533-c1e2-4fc7-ab1c-b62af9e92dd6'::uuid, 'e52583e6-d622-411a-b8f3-c053c487c8f5'::uuid, 4, 'Main Content', '13-20s', 'CARA MELAKUKANNYA!', 'Mau coba? [encouraging tone] Simpan gadget, cari aktivitas seru seperti olahraga atau memasak! Tag teman kalian untuk ikut ya!', 'Medium shot dengan gerakan tangan menunjukkan aktivitas seru dan ajakan untuk beraksi.', 'Encourage audience interaction with a call to action.', 4, '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', '2025-07-20 13:19:05.590', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('48b25f3c-073b-42a4-a1ff-3022cf0a03e1'::uuid, 'cb9cdeaf-5a08-4790-892c-bea7a1af8ff1'::uuid, 2, 'Main Content', '3-10s', 'TIPS #1: TULIS LIST TO-DO!', 'Langkah pertama adalah menulis LIST TO-DO kalian, guys. [excited tone] Ini bikin kalian lebih fokus dan terorganisir.', 'Medium shot menampilkan tangan menulis di buku catatan dengan pulpen berwarna.', 'Pastikan tulisan terlihat jelas', 2, '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9f849fdc-34e8-43f1-a2de-44c7ff209654'::uuid, 'cb9cdeaf-5a08-4790-892c-bea7a1af8ff1'::uuid, 3, 'Main Content', '10-15s', 'TIPS #2: SET JAM KERJA!', 'Setelah itu, tentukan jam kerja kalian. [serious tone] Misalnya, kerja dari jam 9 pagi sampai 5 sore. Ini membantu batasan waktu.', 'Close-up jam dinding yang menunjukkan waktu, dengan tangan menunjuk jam.', 'Tunjukkan para mahasiswa atau pekerja yang mengatur jam di planner', 3, '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0317f823-0506-41b8-8535-81d49314770c'::uuid, 'cb9cdeaf-5a08-4790-892c-bea7a1af8ff1'::uuid, 4, 'Main Content', '15-20s', 'LAST TIP: PRIORTASK KAMU!', 'Terakhir, tentukan PRIORITAS tugas yang paling penting. [excited tone] Ini akan memudahkanmu selama minggu!', 'Medium shot menunjukkan checklist dengan tanda centang di tugas yang sudah selesai.', 'Gunakan animasi untuk menunjukkan perubahan checklist', 4, '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b588215e-72e0-4059-b6d6-5a3bc4f27dcb'::uuid, 'cb9cdeaf-5a08-4790-892c-bea7a1af8ff1'::uuid, 5, 'Main Content', '20-25s', 'AYO RENCANAKAN BERSAMA!', 'Jadi, yuk rencanakan minggu kerja kalian bareng-bareng malam ini! [strong CTA] Komen di bawah apa yang kalian rencanakan!', 'Wide shot dengan creator mengajak penonton sambil tersenyum.', 'Ajak penonton untuk berinteraksi', 5, '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', '2025-07-20 13:19:36.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a2a8a8db-5e1f-44eb-b3ba-19a93422c214'::uuid, 'b23d8585-5dca-4523-b6a8-21568e3575bf'::uuid, 2, 'Main Content', '3-8s', 'Apa itu SMART?', 'Oke, langsung saja! SMART itu singkatan dari Spesifik, Measurable, Achievable, Realistic, dan Time-bound. [excited tone] Mari kita bahas satu per satu!', 'Medium shot dengan papan putih di belakang, dan penanda untuk menulis setiap poin saat dijelaskan.', 'Gunakan aksesoris edukatif seperti papan tulis atau post-it', 2, '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b2bac099-c1ea-41a1-807e-25db351d8001'::uuid, 'b23d8585-5dca-4523-b6a8-21568e3575bf'::uuid, 3, 'Main Content', '8-15s', 'Contoh SMART', 'Contohnya, alih-alih bilang ‘Saya mau sehat’, ubah jadi ‘Saya mau olahraga 3 kali seminggu selama 30 menit’. [excited tone] Ini lebih SMART!', 'Close-up dengan grafik ‘Before’ dan ‘After’ untuk menunjukkan perbandingan goal.', 'Buat visual yang menarik untuk perbandingan', 3, '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('5a7d3145-663e-4a9c-8d29-590df50f3bc8'::uuid, 'b23d8585-5dca-4523-b6a8-21568e3575bf'::uuid, 4, 'Main Content', '15-20s', 'Tentukan Goalmu!', 'Yuk, coba buat goal SMART kalian sendiri! [encouraging tone] Tulis di kolom komentar, dan jangan lupa follow untuk tips selanjutnya!', 'Wide shot dengan tangan diangkat dan senyuman lebar, background cerah untuk menunjukkan semangat.', 'Ajak audience untuk berinteraksi dengan pertanyaan', 4, '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', '2025-07-20 13:20:05.462', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4345ad03-47b1-4d51-8a77-c6799e586fce'::uuid, 'bbf1c073-6da1-4eec-b861-23571040662c'::uuid, 2, 'Main Content', '3-8s', 'BAHAN-BAHAN', 'Pertama, kita butuh MIE KERING, sayuran seperti wortel dan kol, serta bumbu seperti KECAP MANIS, GARLIC, dan CABAI!', 'Medium shot menampilkan bahan-bahan di meja, dengan close-up saat menunjukkan tiap bahan...', 'Tunjukkan setiap bahan satu per satu, tambah dengan teks overlay.', 2, '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e925c107-d4d4-46e3-98fb-fa501c4a24f1'::uuid, 'bbf1c073-6da1-4eec-b861-23571040662c'::uuid, 3, 'Main Content', '8-15s', 'CARA MEMASAK', 'Rebus MIE KERING selama 3 menit, tiriskan, lalu tumis dengan bumbu! Campur semua hingga merata!', 'Medium shot saat merebus mie, kemudian beralih ke panci di atas kompor, menunjukkan proses menumis...', 'Gunakan suara sizzle saat menumis untuk meningkatkan daya tarik.', 3, '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('f87739e1-2907-40d3-a797-24ccee839e79'::uuid, 'bbf1c073-6da1-4eec-b861-23571040662c'::uuid, 4, 'Main Content', '15-20s', 'PENYAJIAN', 'Sajikan MIE GORENG dengan bahan pelengkap seperti telur mata sapi dan taburan bawang goreng. Selamat menikmati!', 'Close-up menampilkan mie goreng yang disajikan dalam piring, ada telur mata sapi di atasnya, dengan garnish...', 'Arahkan kamera dari atas untuk memperlihatkan semua detail penyajian.', 4, '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d9be559b-4208-4abe-bda9-619890745e86'::uuid, 'bbf1c073-6da1-4eec-b861-23571040662c'::uuid, 5, 'Main Content', '20-25s', 'JANGAN LUPA LIKE!', 'Kalau kalian suka video ini, jangan lupa untuk LIKE dan FOLLOW untuk resep lainnya ya!', 'Wide shot, menunjukkan host tersenyum sambil mengangkat jari jempol, latar belakang dapur...', 'Tunjukkan semangat untuk berinteraksi dengan audiens.', 5, '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', '2025-07-20 13:20:34.012', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('de15c944-fe5c-4792-adcb-af33d84557d8'::uuid, '843b2db8-a147-4c29-8644-ff8fca2901d9'::uuid, 2, 'Main Content', '3-8s', 'TIP #1: PLAN!', 'Pertama, RENCANAKAN MENU kalian! Pilih 3-4 jenis makanan untuk seminggu, itu sudah cukup. [informative tone]', 'Medium shot menunjukkan papan tulis atau catatan menu dengan daftar bahan.', 'Engage viewers by pointing to the menu list.', 2, '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('10e9f99a-98ee-4ad5-bffe-c7670a45cde0'::uuid, '843b2db8-a147-4c29-8644-ff8fca2901d9'::uuid, 3, 'Main Content', '8-15s', 'TIP #2: BELI BAHAN!', 'Kedua, BELI bahan-bahan segar! Pastikan sayur dan protein kalian berkualitas. [energetic tone]', 'Wide shot di pasar atau supermarket, memperlihatkan proses pemilihan bahan.', 'Show excitement while selecting fresh produce.', 3, '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('21d263e0-5a15-4ad8-8680-eb5a2dccd500'::uuid, '843b2db8-a147-4c29-8644-ff8fca2901d9'::uuid, 4, 'Main Content', '15-20s', 'TIP #3: SIMPAN DENGAN TEPAT!', 'Terakhir, SIMPAN makanan dalam wadah kedap udara untuk menjaga kesegaran. [serious tone]', 'Close-up menunjukkan wadah tertutup rapat, lalu menunjukkan tempat penyimpanan di kulkas.', 'Use a hand gesture to indicate sealing containers.', 4, '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('49df0ec6-8d10-441a-b591-11ea2902da21'::uuid, '843b2db8-a147-4c29-8644-ff8fca2901d9'::uuid, 5, 'Call to Action', '20-25s', 'IKUTI UNTUK LEBIH BANYAK TIPS!', 'Jadi, ayo mulai meal prep dan rasakan manfaatnya! Jangan lupa follow untuk tips lebih banyak! [inviting tone]', 'Medium shot dengan tangan melambai, latar belakang menunjukkan makanan siap saji.', 'Smile and engage directly to the camera for a strong CTA.', 5, '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', '2025-07-20 13:21:04.711', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ee27bb21-a8f8-47e9-ba22-55bbfff7f51d'::uuid, 'c62c7c57-75d9-44c0-9bb1-4d2196cd8c96'::uuid, 2, 'Main Content', '3-8s', 'BAHAN-BAHAN', 'Pertama, siapkan 2 SENDOK KOPI instan, 2 SENDOK GULA, dan 2 SENDOK AIR panas. Gampang kan?', 'Medium shot menampilkan semua bahan di meja, dengan close-up saat menunjukkan setiap bahan.', 'Point to each ingredient as you mention it', 2, '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c39174a3-4c72-4611-ace4-ec30b6e72bb0'::uuid, 'c62c7c57-75d9-44c0-9bb1-4d2196cd8c96'::uuid, 3, 'Main Content', '8-13s', 'MIXING TIME!', 'Selanjutnya, campurkan semuanya dalam wadah. Kocok dengan mixer sampai berwarna CREAMY dan kental! [excited tone]', 'Zoom in pada mixer yang berputar, dengan fokus pada campuran yang berubah warna.', 'Show enthusiasm while mixing', 3, '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b12c4cb8-8658-4b2e-bf1a-4c7eb38851bf'::uuid, 'c62c7c57-75d9-44c0-9bb1-4d2196cd8c96'::uuid, 4, 'Main Content', '13-18s', 'SIAP DISAJIKAN', 'Tuang campuran Dalgona di atas susu dingin. Dan... TADA! Dalgona Coffee CREAMY siap dinikmati! [joyful tone]', 'Wide shot menunjukkan gelas susu dingin dengan Dalgona di atasnya, kameranya berputar 360 derajat.', 'End with a satisfied expression while tasting', 4, '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0e650bb6-9223-4ebe-8863-a9db03b778da'::uuid, 'c62c7c57-75d9-44c0-9bb1-4d2196cd8c96'::uuid, 5, 'Main Content', '18-20s', 'JANGAN LUPA LIKE!', 'Kalau suka video ini, jangan lupa LIKE dan FOLLOW untuk resep lainnya! Sampai jumpa!', 'Close-up wajah sambil melambaikan tangan dan tersenyum.', 'Encourage engagement with a friendly call to action', 5, '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', '2025-07-20 13:21:31.275', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('480fd492-b68c-4509-8a66-954046a78e48'::uuid, '1dd06f8f-2463-4256-a2b4-aeab6fac32c8'::uuid, 2, 'Main Content', '3-8s', 'BAHAN YANG DIPERLUKAN', 'Pertama, kita butuh bahan-bahan ini: steak, garam, merica, dan sedikit minyak. [excited tone] Gampang kan?', 'Wide shot menunjukkan semua bahan di meja, dengan penekanan pada steak.', 'Organize ingredients neatly for the visual.', 2, '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9971386b-4a61-4f23-898d-423ce5b03a20'::uuid, '1dd06f8f-2463-4256-a2b4-aeab6fac32c8'::uuid, 3, 'Main Content', '8-13s', 'PERSIAPKAN STEAK', 'Selanjutnya, bumbui steak dengan SALT dan PEPPER secukupnya. [instructional tone] Pastikan semua sisi terlapisi rata ya.', 'Medium shot dengan tangan bumbu steak, close-up saat menaburkan garam dan merica.', 'Show close-up actions to highlight the process.', 3, '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('594cae73-6f8a-4c1b-a57c-c2f0fc8d24cf'::uuid, '1dd06f8f-2463-4256-a2b4-aeab6fac32c8'::uuid, 4, 'Main Content', '13-18s', 'MASAK STEAK', 'Panaskan wajan dengan minyak di atas api besar. [energetic tone] Setelah itu, masak steak selama 4-5 menit di setiap sisi untuk mendapatkan medium-rare yang sempurna!', 'Medium shot menunjukkan wajan di atas kompor, steak dibalik saat memasak.', 'Use sizzling sounds for better effect.', 4, '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7b74def4-7b74-4f62-8642-a65960fb66d6'::uuid, '1dd06f8f-2463-4256-a2b4-aeab6fac32c8'::uuid, 5, 'Main Content', '18-23s', 'SIAP DISAJIKAN!', 'Terakhir, biarkan steak istirahat selama 5 menit sebelum diiris. [satisfied tone] Siap disajikan dengan sayuran segar!', 'Wide shot steak yang sudah matang dengan garnish sayuran, close-up saat cara mengiris steak.', 'Highlight the final presentation.', 5, '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', '2025-07-20 13:22:26.565', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9e041f5e-7e1e-40bc-b370-b7174ab4e47e'::uuid, 'ab4f5488-36a4-4743-9cd5-a46601285cff'::uuid, 2, 'Main Content', '3-8s', 'Bahan-Bahan', 'Pertama-tama, kalian butuh brokoli SEGAR, bawang putih, dan sedikit minyak. SANGAT mudah kan?', 'Medium shot menunjukkan bahan-bahan di atas meja, gentle pan untuk memperlihatkan setiap bahan.', 'Highlight each ingredient clearly', 2, '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4f82b6ce-fb67-4811-aa4c-025a1ebb3b15'::uuid, 'ab4f5488-36a4-4743-9cd5-a46601285cff'::uuid, 3, 'Main Content', '8-15s', 'Proses Memasak', 'Panaskan minyak di wajan. Tambahkan bawang putih hingga harum. Lalu, masukkan brokoli dan aduk ADUKEAN selama 5 MENIT!', 'Close-up saat memasukkan bawang putih ke wajan, dengan api menyala, lalu menyorot saat brokoli ditambahkan.', 'Use sizzling sound effects for emphasis', 3, '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1bc608e2-e97b-4228-b70c-463ebdf0d4a7'::uuid, 'ab4f5488-36a4-4743-9cd5-a46601285cff'::uuid, 4, 'Main Content', '15-22s', 'Siap Disajikan!', 'Taraa! TUMIS BROKOLI siap disajikan! SEHAT dan CEPAT! Cobain deh!', 'Wide shot menampilkan piring tumis brokoli yang sudah jadi, ditambahkan hiasan sesuka hati.', 'Show the final dish with a satisfied expression', 4, '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ee31f0e1-d7c8-432f-bfa0-40727738fb3a'::uuid, 'ab4f5488-36a4-4743-9cd5-a46601285cff'::uuid, 5, 'Call to Action', '22-25s', 'LIKE & SHARE!', 'Jangan lupa LIKE dan SHARE video ini! Selamat mencoba di rumah!', 'Medium shot dengan jari menunjuk ke arah kamera, ekspresi ceria.', 'Encourage viewer interaction warmly', 5, '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', '2025-07-20 13:23:02.265', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('45c01e4b-f352-4ec5-9231-f462fb95f0eb'::uuid, 'e56a9ad1-940c-47b9-b9ea-0930fb058d64'::uuid, 2, 'Main Content', '3-10s', 'SAUS SAMBAL SOLO', 'Saus sambal solo ini simpel banget! Cukup campurkan CABAI MERAH, BAWANG PUTIH, dan gula. Ulek hingga halus dan siap disajikan.', 'Medium shot dari bahan-bahan dicampur di cobek, close-up saat diulek.', 'Tunjukkan langkah secara jelas dan tidak terburu-buru', 2, '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ca0a7df7-b325-4df3-8dad-d89b74e402ec'::uuid, 'e56a9ad1-940c-47b9-b9ea-0930fb058d64'::uuid, 3, 'Main Content', '10-15s', 'SAUS SAMBAL TOMAT', 'Selanjutnya, saus sambal tomat! Campurkan TOMAT, CABAI, dan sedikit garam. Blender sampai halus, dan rasakan kelezatannya!', 'Medium shot saat memotong tomat dan cabai, kemudian close-up saat diblender.', 'Gunakan efek suara blender untuk menambah kesan', 3, '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('090f9c48-f611-46c9-b61c-e85033f08bdd'::uuid, 'e56a9ad1-940c-47b9-b9ea-0930fb058d64'::uuid, 4, 'Main Content', '15-20s', 'SAUS SAMBAL ASAM MANIS', 'Terakhir, saus sambal asam manis! Campurkan CABAI, GULA MERAH, dan VINEGAR. Ulek hingga mengental. Berani coba?', 'Medium shot menunjukkan cara mencampur bahan-bahan sambil mengaduk di mangkuk.', 'Ajak penonton untuk berinteraksi dengan pertanyaan', 4, '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', '2025-07-20 13:23:33.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('21aa46fb-5ad9-427e-905b-0a7334c5f636'::uuid, '02d40f41-4ed1-4d1b-abd0-76f8110e6ef3'::uuid, 2, 'Main Content', '3-20s', 'BAHAN-BAHAN', 'Pertama, kita butuh 4 OREO, 1/2 cangkir susu, dan 1/4 cangkir tepung. Gampang kan? Yuk, hancurkan OREO-nya terlebih dahulu!', 'Close-up pada Oreos yang dihancurkan dengan hands-on, lalu diadu ke mug.', 'Tunjukkan gerakan hancurkan dan tampung di mug dengan semangat.', 2, '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('faa78150-5c8b-4c3f-b498-b06326eb4981'::uuid, '02d40f41-4ed1-4d1b-abd0-76f8110e6ef3'::uuid, 3, 'Main Content', '20-40s', 'MENCAMPUR!', 'Sekarang, tambahkan susu ke dalam mug! Campur semua bahan hingga halus, guys. Jangan lupa, semakin rata semakin enak!', 'Medium shot dengan tangan mencampur adonan menggunakan sendok, fokus pada tekstur adonan.', 'Buat gerakan mencampur yang menarik!', 3, '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1ca1d4cb-235e-45ba-bd4b-a54c696e1095'::uuid, '02d40f41-4ed1-4d1b-abd0-76f8110e6ef3'::uuid, 4, 'Main Content', '40-60s', 'PANGGANG!', 'Sekarang, kita masukkan mug ke dalam microwave selama 1 menit. Voila! Mug cake siap disajikan!', 'Wide shot fokus pada microwave dengan mug di dalamnya. Timer terlihat menghitung mundur.', 'Tampilkan momen penantian dengan dramatis.', 4, '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('050043de-389e-42c2-b729-7c9b958e5825'::uuid, '02d40f41-4ed1-4d1b-abd0-76f8110e6ef3'::uuid, 5, 'Main Content', '60-80s', 'SIAP DISAJIKAN!', 'Setelah matang, tambahkan sedikit krim dan remah OREO di atasnya sebagai topping. Selamat menikmati OREO MUG CAKE yang lezat ini!', 'Medium shot saat menambahkan topping di mug cake dengan close-up saat menambahkan remah OREO.', 'Tunjukkan ekspresi bahagia saat mencicipi!', 5, '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('22cf1313-6458-4828-b9f3-0ef73f40d32b'::uuid, '02d40f41-4ed1-4d1b-abd0-76f8110e6ef3'::uuid, 6, 'Call to Action', '80-90s', 'Coba dan Share!', 'Jangan lupa untuk coba di rumah dan SHARE video ini sama teman-teman kalian! Sampai jumpa di resep selanjutnya! [excited tone]', 'Wide shot dengan host melambaikan tangan ke kamera sambil tersenyum.', 'Ajak audiens untuk berinteraksi kembali.', 6, '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', '2025-07-20 13:24:07.021', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e0723364-b7f9-4275-8b26-a14ba4107d04'::uuid, 'c18b9328-0ecc-48ef-8451-70f12c3574c6'::uuid, 2, 'Main Content', '3-8s', 'TIPS #1: UKURAN PISAU!', 'Pertama, kalian harus pilih ukuran yang sesuai! Untuk sayuran, pisau kecil cukup. Untuk daging, ambil yang lebih besar. [informative tone]', 'Medium shot menampilkan dua pisau, satu kecil dan satu besar, dengan tangan menunjuk masing-masing.', 'Highlight with hand movements to emphasize differences.', 2, '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('657aeaa6-5d8c-4f7d-a37c-c9bf9e342188'::uuid, 'c18b9328-0ecc-48ef-8451-70f12c3574c6'::uuid, 3, 'Main Content', '8-13s', 'TIPS #2: BAHAN PISAU!', 'Kedua, perhatikan bahan pisaunya! Stainless steel lebih awet dan ringan, sementara keramik lebih tajam! Pilih yang sesuai kebutuhannya! [explanatory tone]', 'Close-up berbagai bahan pisau, dengan zoom in pada area tajam.', 'Use graphics or animations to show material differences.', 3, '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('550df02b-ccc9-49ca-a18e-f0e3811c2274'::uuid, 'c18b9328-0ecc-48ef-8451-70f12c3574c6'::uuid, 4, 'Main Content', '13-18s', 'MERAWAT PISAU!', 'Jangan lupa! Setelah digunakan, cuci pisau dengan tangan, lap kering, dan simpan di tempatnya. Ini penting agar pisaunya awet! [caring tone]', 'Medium shot mencuci pisau di wastafel, lalu mengeringkannya dengan kain bersih.', 'Demonstrate the cleaning process clearly.', 4, '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('694cd9be-a319-4307-88ff-bfaa67b3ebb4'::uuid, 'c18b9328-0ecc-48ef-8451-70f12c3574c6'::uuid, 5, 'Main Content', '18-20s', 'YUK PRAKTEK!', 'Sekarang, saatnya kalian praktek! Jangan lupa like dan share jika video ini bermanfaat! [excited tone]', 'Wide shot diri sendiri mengajak viewers untuk mencoba di dapur, dengan senyum lebar.', 'End with a strong call to action and a smile.', 5, '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', '2025-07-20 13:24:41.302', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cbd39e6d-2489-48dd-8339-dfee89ce1e8c'::uuid, 'e4244740-d32f-4a7a-a3e5-cd833a22da47'::uuid, 2, 'Main Content', '3-8s', 'Bumbu Rahasia!', 'OKE! Rahasia pertama adalah bumbu! Gunakan KECAP MANIS yang berkualitas! Ini bikin rasa lebih NENDANG! [excited tone]', 'Medium shot dari tangan menuang kecap manis ke dalam wajan dengan efek slow motion.', 'Show close-up of the kecap manis bottle.', 2, '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('5b9899ae-c8ab-4877-9628-deea9d02ff4f'::uuid, 'e4244740-d32f-4a7a-a3e5-cd833a22da47'::uuid, 3, 'Main Content', '8-13s', 'Kombinasi Bahan!', 'Kedua, campuran bahan. Jangan lupa tambahkan SAYURAN segar dan TELUR, ini bikin nasi goreng lebih LEZAT dan bergizi! [enthusiastic tone]', 'Wide shot menyiapkan sayuran dengan zoom in pada telur yang sedang dipecahkan.', 'Use bright lighting to highlight fresh ingredients.', 3, '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('789bd1aa-e533-4f46-bba7-e5373bbdd31d'::uuid, 'e4244740-d32f-4a7a-a3e5-cd833a22da47'::uuid, 4, 'Main Content', '13-18s', 'Teknik Memasak!', 'Terakhir, teknik memasak! Aduk cepat selama 3-5 menit di API BESAR untuk cita rasa yang otentik! [excited tone]', 'Medium shot memperlihatkan proses menggoreng sambil menyalakan api besar.', 'Use fast cuts to create a lively cooking scene.', 4, '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('81af75a5-7e5d-4786-9fb6-46a12c6800bf'::uuid, 'e4244740-d32f-4a7a-a3e5-cd833a22da47'::uuid, 5, 'Main Content', '18-23s', 'Hasil Akhir!', 'Voila! Ini dia Nasi Goreng ala RESTORAN yang siap dinikmati! Jangan lupa coba di rumah ya! [excited tone]', 'Wide shot menampilkan nasi goreng di piring cantik, dengan garnish yang menarik.', 'Show a final shot with a smile, serving the dish elegantly.', 5, '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', '2025-07-20 13:25:13.196', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('56a13515-53a7-4282-9925-12dae8a1447e'::uuid, '63990380-f319-4fbc-9671-0bcdda48de0a'::uuid, 2, 'Main Content', '3-8s', 'Gunakan Piring Bersih', 'Pertama, pastikan kalian menggunakan piring yang bersih dan sesuai tema. Pilih piring berwarna netral agar makanan terlihat lebih menonjol. CONTEX adalah kuncinya!', 'Medium shot memperlihatkan piring bersih, diatur di atas meja dengan latar belakang simple.', 'Tunjukkan piring yang berbeda-beda untuk variasi!', 2, '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c4366f07-3fbc-490a-a1a6-e9e0cebd8eeb'::uuid, '63990380-f319-4fbc-9671-0bcdda48de0a'::uuid, 3, 'Main Content', '8-13s', 'Atur Makanan dengan Cermat', 'Selanjutnya, atur makanan di piring dengan cermat. Letakkan makanan utama di tengah, dan susun pelengkap di sekitar untuk menciptakan DIMENSI.', 'Wide shot menunjukkan proses penyusunan makanan dengan tangan meletakkan setiap elemen.', 'Gunakan teknik ''tinggi dan rendah'' untuk menarik perhatian!', 3, '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('169faf85-3630-49d0-b721-c85cdeafbd5d'::uuid, '63990380-f319-4fbc-9671-0bcdda48de0a'::uuid, 4, 'Main Content', '13-18s', 'Sentuhan Akhir', 'Terakhir, jangan lupa tambahkan garnish! Sepercik saus atau hiasan herbs bisa membuat plating kalian jadi lebih MENAWAN. Ingat, PERHATIAN pada detail itu penting!', 'Extreme close-up saat menambahkan garnish, dengan cahaya ring light yang memantul indah.', 'Gunakan gerakan lembut saat menambahkan garnish!', 4, '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a2015448-300c-4fc6-a662-4e36192b57c0'::uuid, '63990380-f319-4fbc-9671-0bcdda48de0a'::uuid, 5, 'Call to Action', '18-20s', 'Jangan Lupa Share!', 'Nah, itu dia tips plating aesthetic! Kalo kalian suka, jangan lupa untuk LIKE dan SHARE video ini ya! Sampai jumpa!', 'Wide shot dengan tangan melambai dan smile, kamera mundur menjauh dari meja.', 'Ajak audiens untuk interaksi di akhir!', 5, '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', '2025-07-20 13:25:46.996', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9e0d9908-478b-4544-b6a7-027a24f7f383'::uuid, 'd76b5366-0a1f-4d59-a9bf-27ac38060b04'::uuid, 2, 'Main Content', '3-10s', '1. PLANK', 'Oke, kita mulai dengan PLANK! [excited tone] Tahan posisi ini selama 30 DETIK. Ini akan menguatkan inti perut kamu!', 'Medium shot menunjukkan demonstrasi plank dengan fokus di otot perut.', 'Hold your position firm and maintain a strong posture', 2, '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('338898cb-00cf-4c6d-b1d3-8eab8452b9d7'::uuid, 'd76b5366-0a1f-4d59-a9bf-27ac38060b04'::uuid, 3, 'Main Content', '10-15s', '2. SIT UP', 'Selanjutnya, SIT UP! [energized tone] Lakukan 15 kali. Pastikan kamu tarik napas saat turun dan hembuskan saat naik!', 'Wide shot menunjukkan demonstrasi sit up dengan perut mengencang.', 'Breathe to enhance performance and maintain rhythm', 3, '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0690cfe1-fe91-420a-a587-b0a612a1d440'::uuid, 'd76b5366-0a1f-4d59-a9bf-27ac38060b04'::uuid, 4, 'Main Content', '15-20s', '3. LEG RAISE', 'Terakhir, LEG RAISE! [enthusiastic tone] Lakukan 10 kali. Jaga kaki tetap lurus dan angkat perlahan!', 'Medium shot menunjukkan demonstrasi leg raise dengan fokus pada gerakan.', 'Control your movement to maximize effectiveness', 4, '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('24b28e89-39d3-4266-ae0c-a8744f056750'::uuid, 'd76b5366-0a1f-4d59-a9bf-27ac38060b04'::uuid, 5, 'Main Content', '20-25s', 'SELAMAT MENCOBA!', 'Nah, itu dia! [cheerful tone] Cuma 7 MENIT bisa bikin kamu lebih bugar! Jangan lupa untuk LIKE dan FOLLOW untuk tips lainnya!', 'Close-up wajah sambil tersenyum, memberi thumbs up, dan logo di akhir.', 'End with a call to action and a positive note', 5, '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', '2025-07-20 13:26:21.286', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('491a82ad-bddb-4415-ab2c-d28ad3ffb427'::uuid, '7b7675b9-cbb5-4343-82fe-ca20b9a434ee'::uuid, 2, 'Main Content', '3-8s', 'Tip Stretching #1', 'Pertama, coba ini: duduk tegak dan tarik napas dalam. Saat mengeluarkan napas, angkat lengan kalian tinggi-tinggi. Ini bisa membantu meredakan ketegangan di punggung atas kalian! [informative tone]', 'Medium shot memperlihatkan posisi duduk yang benar, demonstrasi gerakan tangan.', 'Tunjuk lengan ke atas untuk penekanan pada gerakan', 2, '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b02757dd-37da-4ea3-abec-f12ca6377278'::uuid, '7b7675b9-cbb5-4343-82fe-ca20b9a434ee'::uuid, 3, 'Main Content', '8-13s', 'Tip Stretching #2', 'Kedua, untuk leher! Perlahan putar leher ke kiri dan kanan. Rasakan otot leher kalian meregang. Ini mencegah nyeri leher saat bekerja! [engaging tone]', 'Close-up wajah saat melakukan gerakan leher, dengan ekspresi tenang.', 'Fokus pada ekspresi wajah yang rileks', 3, '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c8c6031c-45f6-4804-8055-152bf5765715'::uuid, '7b7675b9-cbb5-4343-82fe-ca20b9a434ee'::uuid, 4, 'Main Content', '13-18s', 'Tip Stretching #3', 'Terakhir, cobalah merentangkan kaki kalian! Berdiri, dan sejajarkan kaki kalian, lalu tekuk sedikit lutut. Ini membantu memperbaiki aliran darah! [enthusiastic tone]', 'Wide shot menunjukkan posisi berdiri yang benar, dengan latar belakang meja kerja.', 'Gerakan tubuh harus terlihat alami dan leluasa', 4, '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6d9ed63b-ea75-406b-afd2-297e1e06cf3d'::uuid, '7b7675b9-cbb5-4343-82fe-ca20b9a434ee'::uuid, 5, 'CTA', '18-25s', 'Yuk, stretch bareng!', 'Nah, itu dia tipsnya! Jangan lupa untuk stretching setiap jam, biar nyaman saat bekerja! Like dan share video ini ke teman-teman kalian! [excited tone]', 'Medium shot dengan senyuman, melambaikan tangan, latar belakang meja kerja.', 'Akhiri dengan senyuman dan ajakan untuk berinteraksi', 5, '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', '2025-07-20 13:26:51.765', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('275f4319-80d8-4b52-ae64-03f8e4d8d5d2'::uuid, '76f5d625-a8b9-411a-a673-ae2e3dc0220b'::uuid, 2, 'Main Content', '3-8s', 'Gerakan 1: Burpees', 'Gerakan pertama adalah BURPEES! [excited tone] Ini adalah gerakan kombinasi yang super efektif untuk membakar kalori. Coba lakukan selama 30 detik!', 'Medium shot menunjukkan demonstrasi gerakan burpees dengan penekanan pada setiap langkah.', 'Tunjukkan teknik dengan jelas dan enerjik.', 2, '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('02456f5f-ebe4-448c-bb49-755146079bfc'::uuid, '76f5d625-a8b9-411a-a673-ae2e3dc0220b'::uuid, 3, 'Main Content', '8-13s', 'Gerakan 2: Jumping Jacks', 'Selanjutnya, kita punya JUMPING JACKS! [upbeat tone] Lakukan ini dan rasakan detak jantungmu meningkat. Ayo, keep going selama 30 detik!', 'Wide shot dengan gerakan jumping jacks berulang, menambahkan semangat.', 'Gunakan musik yang enerjik untuk meningkatkan suasana.', 3, '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e3a15d8f-6725-4712-8e7f-5e58a9041b53'::uuid, '76f5d625-a8b9-411a-a673-ae2e3dc0220b'::uuid, 4, 'Main Content', '13-18s', 'Gerakan 3: High Knees', 'Gerakan ketiga adalah HIGH KNEES! [energetic tone] Ini bagus untuk melatih otot kaki sambil membakar kalori. Lakukan sampai 30 detik ya!', 'Close-up dari gerakan high knees dengan fokus pada kaki dan gerakan lengan.', 'Pastikan untuk menekankan setiap detakan kaki dengan energik.', 4, '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('5538d138-d4d1-4aa9-9664-4e6692f19e69'::uuid, '76f5d625-a8b9-411a-a673-ae2e3dc0220b'::uuid, 5, 'Main Content', '18-23s', 'Gerakan 4 & 5: Mountain Climbers & Squat Jumps', 'Dan terakhir, kita punya MOUNTAIN CLIMBERS dan SQUAT JUMPS! [excited tone] Keduanya efektif untuk membakar kalori! Coba lakukan masing-masing selama 30 detik!', 'Split screen menunjukkan dua gerakan sekaligus, energik dan penuh semangat.', 'Fokus pada aliran gerakan dan menunjukkan hasil.', 5, '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bd7c647d-ca31-4212-a8d2-9da1330b3dfc'::uuid, '76f5d625-a8b9-411a-a673-ae2e3dc0220b'::uuid, 6, 'Closing', '23-25s', 'Ayo coba sekarang!', 'Jadi, siap berlatih? [motivational tone] Coba 5 gerakan ini dan lihat hasilnya! Jangan lupa like dan follow untuk lebih banyak tips!', 'Medium shot kembali ke wajah, memberi semangat dan motivasi.', 'Ajak pemirsa untuk berinteraksi dengan CTA yang jelas.', 6, '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', '2025-07-20 13:27:27.019', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('3de94244-8a2d-43f2-9556-f15c2c203a27'::uuid, 'b2f59a20-2b30-44f4-91e4-be18b2781ecc'::uuid, 2, 'Main Content', '3-10s', 'LANGKAH 1: POSISI DUDUK YANG BENAR', 'Langkah pertama, pastikan punggung kalian tegak, bahu rileks, dan kaki rata di lantai. [encouraging tone] Jangan mencondongkan badan ke depan!', 'Medium shot dengan demonstrasi posisi duduk yang benar, menunjukkan postur tubuh yang ideal.', 'Tunjukkan gerakan tubuh yang tepat dan saksikan perbedaannya.', 2, '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1dfcf140-8fa1-443c-8c01-a6e62f43c416'::uuid, 'b2f59a20-2b30-44f4-91e4-be18b2781ecc'::uuid, 3, 'Main Content', '10-15s', 'LANGKAH 2: ISTIRAHAT RUTIN', 'Yang kedua, ingatlah untuk berdiri dan peregangan setiap 30 menit. [motivating tone] Langkah kecil ini membantu mencegah rasa sakit!', 'Wide shot saat berdiri dan meregangkan tubuh, menunjukkan contoh gerakan sederhana.', 'Gunakan latar belakang musik energik untuk membuatnya lebih menarik.', 3, '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('dbc581f0-6244-457c-b5a6-d46c0910e477'::uuid, 'b2f59a20-2b30-44f4-91e4-be18b2781ecc'::uuid, 4, 'Main Content', '15-20s', 'LANGKAH 3: GUNAKAN ALAT BANTU', 'Lastly, kalian bisa pakai bantal khusus penyangga punggung. [informative tone] Ini benar-benar membantu menjaga postur kalian!', 'Close-up pada bantal penyangga punggung saat meletakkannya di kursi.', 'Tampilkan alat bantu dengan jelas agar penonton dapat melihatnya.', 4, '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', '2025-07-20 13:28:02.516', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e624ffd9-5851-41d4-a647-152137f24feb'::uuid, 'ae76d49e-e767-4ba5-835c-0275f51a141b'::uuid, 2, 'Main Content', '3-10s', 'Gerakan #1: Squat', 'Oke, gerakan pertama adalah SQUAT! Kalian cukup injak band dengan kedua kaki dan pegang kedua ujungnya. [excited tone] Tahan punggung tetap tegak dan turun hingga paha sejajar dengan lantai!', 'Medium shot memperlihatkan demonstrasi squat dengan band, fokus pada posisi kaki dan tangan.', 'Show the correct form clearly for viewers', 2, '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9f371a89-603f-4170-8a52-4bce37dfc9dc'::uuid, 'ae76d49e-e767-4ba5-835c-0275f51a141b'::uuid, 3, 'Main Content', '10-15s', 'Gerakan #2: Bent Over Row', 'Selanjutnya, kita coba BENT OVER ROW! Injak band, ambil posisi merunduk, dan tarik band ke arah dada. [serious tone] Ini bagus untuk punggung dan lengan, guys!', 'Medium shot menunjukkan posisi yang benar dengan penekanan pada otot yang bekerja.', 'Highlight the muscles being worked', 3, '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b1a172c4-63f9-4c54-b8ee-d5a22db477f9'::uuid, 'ae76d49e-e767-4ba5-835c-0275f51a141b'::uuid, 4, 'Main Content', '15-20s', 'Gerakan #3: Chest Press', 'Terakhir, untuk CHEST PRESS, ikat band di belakang punggung. Pegang di depan dan dorong ke depan. [excited tone] Keren kan? Kalian bisa dapat banyak manfaat dari sini!', 'Wide shot menunjukkan keseluruhan gerakan dan bagaimana cara melakukan dengan benar.', 'Encourage viewers to try out the moves themselves', 4, '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', '2025-07-20 13:28:36.638', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('3265900d-edcb-42a5-bb57-6122e7759650'::uuid, 'a1f88c38-3111-460b-926a-f40eceecc15a'::uuid, 2, 'Main Content', '3-8s', 'APA ITU CHALLENGE INI?', 'Challenge PUSH-UP 30 HARI ini cocok untuk semua level! Kita mulai dengan 10 push-up di hari pertama. Gampang kan? Jangan khawatir, kita akan naikkan jumlahnya setiap hari! [excited]', 'Medium shot menunjukkan demonstrasi push-up dengan angka di overlay, bergerak ke arah set berikutnya.', 'Demonstrate proper form while explaining', 2, '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0fbc0205-f75d-4662-9601-2e949d2bb4f0'::uuid, 'a1f88c38-3111-460b-926a-f40eceecc15a'::uuid, 3, 'Main Content', '8-13s', 'TIPS Sukses!', 'Ingat! Selalu lakukan pemanasan sebelum berlatih! [serious tone] Juga, pastikan untuk beristirahat dan tetap terhidrasi. Dengan cara ini, kalian bisa maksimal!', 'Close-up tangan memegang air mineral, kemudian slow zoom out ke medium shot pemanasan.', 'Emphasize the importance of hydration and warm-up', 3, '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d3c0bbd3-da7d-4c50-98e4-8ff87add7ccd'::uuid, 'a1f88c38-3111-460b-926a-f40eceecc15a'::uuid, 4, 'Main Content', '13-18s', 'IKUTI SAYA!', 'Yuk kita jalani bareng! [excited tone] Post hasil 30 harimu dan tag aku! Siap untuk tantangan ini? Ayo mulai sekarang!', 'Wide shot menunjukkan peserta push-up bersama, lalu kembali close-up dengan senyuman.', 'Encourage viewers to join and tag you', 4, '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', '2025-07-20 13:29:14.336', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('658d61ab-5a84-4337-8828-fcf0f4689c3d'::uuid, 'ca27451b-a8ba-46e2-8bba-e75b75430b5f'::uuid, 5, 'Call to Action', '18-25s', 'Siap Investasi Emas?', 'Yuk, mulai investasi emas digital dengan cara yang aman ini! [excited tone] Like dan share video ini ya, guys!', 'Medium shot dengan senyuman lebar, jari telunjuk menunjuk ke kamera...', 'Akhiri dengan aksi positif dan ramah', 5, '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ab707d35-40f4-400b-a412-8c764dc90b06'::uuid, '87694d20-0367-483f-8fda-8a36fc92bd80'::uuid, 2, 'Main Content', '3-10s', 'SARAPAN', 'Pertama, sarapan! [excited] Aku pilih OATMEAL dengan irisan pisang dan sedikit madu. PERFECT untuk energy booster di pagi hari!', 'Medium shot dari atas, menampilkan oatmeal dengan topping pisang dan madu, slow motion saat drizzling madu.', 'Show each ingredient clearly for better engagement.', 2, '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9ffcb7d8-4ca9-4d25-a2db-6a2135850f9a'::uuid, '87694d20-0367-483f-8fda-8a36fc92bd80'::uuid, 3, 'Main Content', '10-15s', 'MAKAN SIANG', 'Untuk makan siang, aku punya NASI MERAH dengan sayuran kukus dan dada ayam. Seimbang dan ENAK! [enthusiastic]', 'Wide shot menampilkan set makanan, fokus pada piring dengan nasi merah dan sayuran, pan ke ayam.', 'Make the food look appealing and vibrant.', 3, '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('fcb1172b-8f33-4d9e-8729-9845fc8d4ddf'::uuid, '87694d20-0367-483f-8fda-8a36fc92bd80'::uuid, 4, 'Main Content', '15-20s', 'SNACK', 'Tapi jangan lupa SNACK! Aku suka BATANG CEREAL dan buah-buahan segar. [cheerful] Menyegarkan dan sehat!', 'Medium shot menunjukkan presenter memegang baton cereal dan berbagai buah, close-up saat menggigit.', 'Highlight snacks as a key element of a balanced diet.', 4, '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9449b3dc-ae0d-4a67-9052-3e72fda4f770'::uuid, '87694d20-0367-483f-8fda-8a36fc92bd80'::uuid, 5, 'Main Content', '20-25s', 'MAKAN MALAM', 'Dan untuk makan malam, aku pilih SUSHI! [excited] Ikan salmon, sayuran segar, dan nasi sushi. Sederhana tapi SANGAT ENAK!', 'Wide shot dari meja dengan sushi, close-up saat menyusun sushi.', 'Conclude with an appealing dinner that ties the day together.', 5, '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('de4c75aa-b4fd-4116-abdd-1ae4de7ffa81'::uuid, '87694d20-0367-483f-8fda-8a36fc92bd80'::uuid, 6, 'Conclusion', '25-30s', 'DIET SEIMBANG, GAMPANG!', 'Itu dia guys! Makan sehat bisa mudah dan enak! Jangan lupa LIKE dan SHARE untuk tips lainnya! [cheerful]', 'Medium shot presenter melambai sambil tersenyum, background warna cerah.', 'End with a call-to-action to encourage audience interaction.', 6, '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', '2025-07-20 13:29:53.800', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bfcaa59c-f26e-4dc0-9b74-5feac9b0ca8a'::uuid, '0d75aaf9-f506-44e9-8e84-483905b1d5f9'::uuid, 2, 'Main Content', '3-10s', 'TIP #1: Target 2-3 Liter', 'Tip pertama, coba targetkan minum 2-3 LITER AIR dalam sehari. Buatlah jadwal minum, seperti setiap jam! [excited tone]', 'Medium shot dengan kamu menunjukkan botol air yang sudah terisi, lalu catat di planner.', 'Use a planner to show organization.', 2, '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cba9f45e-b695-4afd-b368-825ebb8491a5'::uuid, '0d75aaf9-f506-44e9-8e84-483905b1d5f9'::uuid, 3, 'Main Content', '10-15s', 'TIP #2: Bawa Botol Air', 'Kedua, selalu bawa BOTOL AIR kemana-mana. Ini bikin kamu lebih ingat untuk minum! [encouraging tone]', 'Wide shot menunjukkan kamu mengisi botol air dan membawanya ke luar.', 'Show the routine of carrying the bottle.', 3, '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d5c6be6a-de1e-43a6-9b5b-2af14bac423c'::uuid, '0d75aaf9-f506-44e9-8e84-483905b1d5f9'::uuid, 4, 'Main Content', '15-20s', 'TIP #3: Tambahkan Rasa!', 'Terakhir, jika boring, coba tambahkan perasan LEMON atau STRAWBERRY biar lebih segar! [cheerful tone]', 'Close-up pada kamu menuangkan lemon ke dalam gelas air, tampilkan hasilnya dengan senyuman.', 'Focus on the fruits being added.', 4, '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', '2025-07-20 13:30:26.916', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('604aed26-5861-4262-ae37-e758501182df'::uuid, '6020ff28-3774-40a6-904b-bdc0c225c1d3'::uuid, 2, 'Main Content', '3-8s', 'MANFAAT #1', 'Pertama-tama, walk-meeting bikin kita lebih AKTIF! Dengan bergerak, tubuh kita jadi lebih energik, guys. [excited]', 'Medium shot menunjukkan orang berjalan cepat sambil berdiskusi.', 'Tunjukkan gerakan aktif yang menambah energi', 2, '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('84998db7-2ef3-4551-8b31-156f8769d9b5'::uuid, '6020ff28-3774-40a6-904b-bdc0c225c1d3'::uuid, 3, 'Main Content', '8-13s', 'MANFAAT #2', 'Kedua, ini bisa MENINGKATKAN KREATIVITAS. Saat kita di luar ruangan, ide-ide baru bisa bermunculan. Coba deh! [enthusiastic]', 'Wide shot dari jalan hijau dengan dua orang yang berbicara sambil melihat pemandangan.', ' Ganti perspektif dengan menangkap suasana luar', 3, '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('2efac02b-bcad-46b3-bfb2-06cd931e81cb'::uuid, '6020ff28-3774-40a6-904b-bdc0c225c1d3'::uuid, 4, 'Main Content', '13-18s', 'MANFAAT #3', 'Dan terakhir, walk-meeting membantu kita lebih TIDAK STRES. Berjalan jauh dari meja kerja bisa jadi terapi! [relaxed]', 'Medium shot yang menunjukkan orang tersenyum dan menurunkan bahu saat berjalan.', 'Tunjukkan momen relaksasi setelah pertemuan', 4, '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('44a95e9f-01a7-487f-944b-75ab8cad9904'::uuid, '6020ff28-3774-40a6-904b-bdc0c225c1d3'::uuid, 5, 'Call to Action', '18-25s', 'Coba Walk-Meeting!', 'Ayo, coba sekali saja! Ganti suasana dan lihat bagaimana kerja kita bisa semakin menarik. Jangan lupa share pengalaman kalian! [excited]', 'Medium shot dengan gestur tangan mengundang, menunjukkan energi positif.', 'Buat CTA yang kuat dan mengajak interaksi', 5, '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', '2025-07-20 13:31:04.697', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1fc8dc67-00d6-4142-bf15-18483fbbda51'::uuid, '9be732c8-4ffa-44d7-aec8-e2b72e187e2e'::uuid, 2, 'Main Content', '3-10s', 'LANGKAH 1: PERSIAPKAN DIRI', 'Langkah pertama adalah cari tempat yang tenang. Duduklah dengan nyaman, bisa di kursi atau di lantai. Pastikan punggung kalian tegak dan santai. [calm tone]', 'Medium shot dengan posisi duduk yang benar, memperlihatkan punggung tegak dan kaki bersila.', 'Tunjukkan posisi yang benar dengan tangan di lutut.', 2, '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('93896286-4a8b-4335-b01a-7582c18f8233'::uuid, '9be732c8-4ffa-44d7-aec8-e2b72e187e2e'::uuid, 3, 'Main Content', '10-15s', 'LANGKAH 2: FOKUS PADA PERNAPASAN', 'Sekarang, fokuskan perhatian pada pernapasan kalian. Tarik napas dalam-dalam... dan hembuskan perlahan. Rasakan udara masuk dan keluar. [calm tone]', 'Close-up pada wajah yang tenang, fokus pada napas dengan gerakan tangan memperagakan menarik dan menghembuskan napas.', 'Gunakan ekspresi damai, tutup mata saat menarik napas.', 3, '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6307b841-b3c1-4982-b200-fab7e1950e7c'::uuid, '9be732c8-4ffa-44d7-aec8-e2b72e187e2e'::uuid, 4, 'Main Content', '15-20s', 'LANGKAH 3: TUTUP MEDITASI', 'Setelah 5 menit, buka mata kalian dan rasakan ketenangannya. Ingat, meditasi ini bisa kalian ulang setiap hari! [motivational tone]', 'Medium shot setelah membuka mata, tersenyum sambil memberi thumbs up, dengan suasana cerah.', 'Ajak penonton dengan gerakan tangan, memberi tanda bahwa mereka bisa mencobanya.', 4, '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', '2025-07-20 13:31:42.718', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cefb64b5-736a-45d1-ae73-7f9c346528e8'::uuid, 'bb8648d8-a0ee-4e46-873e-90b5b38bb6b3'::uuid, 2, 'Main Content', '3-10s', 'DESAIN MENAWAN', 'Desain smartphone ini menawan dengan build quality yang premium! Kalian pasti bakal merasa Mewah saat pegang!', 'Close-up detail bagian belakang smartphone, panning untuk menyoroti desain.', 'Focus on showing the phone''s design details', 2, '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('700e220e-99b3-448a-8c78-4d1984362c5f'::uuid, 'bb8648d8-a0ee-4e46-873e-90b5b38bb6b3'::uuid, 3, 'Main Content', '10-15s', 'PERFORMANSI SUPER', 'Nah, untuk performansi, smartphone ini dibekali prosesor tercepat di kelasnya! [confident tone] Gak bakal ada lag lagi, guys!', 'Medium shot menunjukkan aplikasi berat diluncurkan dengan cepat di smartphone.', 'Show an app being opened quickly for demonstration', 3, '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('81de3fd9-74f5-4dc7-9d5f-86f76e0fc32b'::uuid, 'bb8648d8-a0ee-4e46-873e-90b5b38bb6b3'::uuid, 4, 'Main Content', '15-20s', 'HARGA & REKOMENDASI', 'Dengan semua fitur ini, harganya juga bersaing! Jadi, apakah kalian siap untuk upgrade? [enthusiastic tone]', 'Wide shot dengan smartphone dan harga yang ditampilkan di layar. Tangan menunjuk ke harga.', 'Conclude with an engaging question to encourage comments', 4, '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', '2025-07-20 13:32:12.334', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('023c12fa-8ecc-4ab3-baa7-db1f4eb9c503'::uuid, 'd3264700-2a3c-43a1-85ea-e3031de81903'::uuid, 2, 'Main Content', '3-8s', 'TIP #1', 'Pertama, JANGAN biarkan laptop kalian terus terhubung ke charger saat sudah penuh. Ini bisa merusak BATERAI!', 'Medium shot dari atas menunjukkan laptop dengan indikator pengisian baterai, zoom in ke persentase baterai.', 'Use visual cues to emphasize the importance of disconnecting the charger.', 2, '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e7f1126a-8b3b-4571-9f31-5464fd966f5a'::uuid, 'd3264700-2a3c-43a1-85ea-e3031de81903'::uuid, 3, 'Main Content', '8-13s', 'TIP #2', 'Kedua, usahakan untuk tidak membiarkan baterai habis total. Isi ulang saat berada di antara 20-80 persen agar BATERAI lebih awet!', 'Wide shot menunjukkan pengguna laptop sambil mengisi daya, dengan grafik kecil di sisi layar menampilkan rentang ideal.', 'Demonstrate the ideal battery range visually.', 3, '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9fbd455b-b697-44cf-a307-d9a50a93398a'::uuid, 'd3264700-2a3c-43a1-85ea-e3031de81903'::uuid, 4, 'Main Content', '13-18s', 'TIP #3', 'Ketiga, gunakan mode hemat daya saat kalian sedang tidak menggunakan laptop, ini bisa membantu menghemat BATERAI!', 'Medium shot menampilkan pengaturan laptop dengan mode hemat daya diaktifkan, close-up pada tombol.', 'Highlight settings visually for better understanding.', 4, '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('1dd912f8-a01f-4ae1-b88e-cc0df3eb012f'::uuid, 'd3264700-2a3c-43a1-85ea-e3031de81903'::uuid, 5, 'Main Content', '18-23s', 'Jangan Lupa!', 'Ingat, guys! Dengan merawat baterai laptop dengan baik, kalian bisa memperpanjang masa penggunaannya. Yuk, coba sekarang juga!', 'Close-up dari tangan pengguna yang menutup laptop dengan senyum puas, menampilkan pesan motivasi di layar.', 'End with a call to action that encourages viewers to apply the tips.', 5, '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', '2025-07-20 13:32:48.429', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('af37feba-a9c4-42a4-af3b-cfcc30865b4c'::uuid, 'd19e09e7-4a74-4fdc-8bdb-93549be138d4'::uuid, 2, 'Main Content', '3-10s', 'AI TOOL #1: CANVA', 'Yang pertama adalah CANVA! [excited tone] Ini adalah tool desain yang sangat mudah digunakan. Dengan berbagai template, kalian bisa bikin poster, presentasi, bahkan video tanpa perlu jadi desainer!', 'Screen recording dari Canva, menunjukkan penggunaan template dan elemen desain.', 'Highlight the interface clearly', 2, '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('dfdd24ea-536e-46c6-ae6c-2ac2b12f0b02'::uuid, 'd19e09e7-4a74-4fdc-8bdb-93549be138d4'::uuid, 3, 'Main Content', '10-17s', 'AI TOOL #2: TYPITO', 'Tool kedua adalah TYPITO! [enthusiastic tone] Dengan TYPITO, kalian bisa bikin video dengan subtitle otomatis. Cocok buat kalian yang sering bikin konten di TikTok!', 'Demo penggunaan Typito dengan video dan subtitle yang muncul secara otomatis.', 'Show before and after using the tool', 3, '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('78314409-066c-444e-a237-2ebe332ef87d'::uuid, 'd19e09e7-4a74-4fdc-8bdb-93549be138d4'::uuid, 4, 'Main Content', '17-24s', 'AI TOOL #3: CHATGPT', 'Yang terakhir, ada CHATGPT! [energetic tone] Ini adalah teman terbaik kalian untuk menulis artikel, brainstorming ide, atau sekedar menjawab pertanyaan. Semua GRATIS dan sangat membantu!', 'Screen recording interaksi dengan ChatGPT, menunjukkan pertanyaan dan jawaban yang cepat.', 'Ensure the text is legible on screen', 4, '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('95d79427-a3f8-407e-bdb2-32a88c83d8f5'::uuid, 'd19e09e7-4a74-4fdc-8bdb-93549be138d4'::uuid, 5, 'Call to Action', '24-25s', 'Coba Sekarang!', 'Jadi, tunggu apa lagi? Coba ketiga AI tool ini sekarang juga! Jangan lupa like dan follow untuk tips teknologi lainnya!', 'Medium shot, menunjukkan thumbs up dan senyuman lebar.', 'Encourage audience engagement', 5, '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', '2025-07-20 13:33:37.013', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7c86261c-c966-42c1-8922-574d89497178'::uuid, 'efade350-2301-45b5-ba6c-ebd43d641154'::uuid, 2, 'Main Content', '3-10s', 'SETTINGS PERTAMA', 'Setting pertama yang wajib kalian atur adalah... RESOLUSI. Pilih 4K untuk hasil yang lebih JELAS. [emphasizing tone] Jangan lupa, atur juga FRAME RATE menjadi 24fps untuk vibe sinematik!', 'Medium shot dengan tampilan layar smartphone, memperlihatkan pengaturan resolusi dan frame rate.', 'Beri penjelasan sambil menunjukkan layar smartphone', 2, '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('f4c864d8-e4c2-4c21-b579-4b889b3ede40'::uuid, 'efade350-2301-45b5-ba6c-ebd43d641154'::uuid, 3, 'Main Content', '10-15s', 'TEMPERATURE WARNA', 'Selanjutnya, atur WHITE BALANCE. [serious tone] Gunakan setting AUTO atau sesuaikan dengan kondisi pencahayaan agar warna tampak NATURAL!', 'Close-up di bagian pengaturan white balance, tampilkan demonstrasi setting yang benar.', 'Pindah-pindah antar pengaturan untuk lebih jelas', 3, '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4be326f3-8dda-493d-94d9-a8eaee80337b'::uuid, 'efade350-2301-45b5-ba6c-ebd43d641154'::uuid, 4, 'Main Content', '15-20s', 'JANGAN LUPA STABILISASI!', 'Terakhir, aktifkan STABILIZER di kamera kalian. [excited tone] Ini sangat membantu hasil video agar tidak goyang saat pengambilan gambar!', 'Medium shot, demonstrasikan video stabilizer aktif dengan pengambilan gambar berjalan.', 'Beri contoh video sebelum dan sesudah stabilisasi', 4, '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('bdc87735-d023-4362-bde1-192d0bff5858'::uuid, 'efade350-2301-45b5-ba6c-ebd43d641154'::uuid, 5, 'CTA', '20-25s', 'IKUTI UNTUK TIP LAIN!', 'Jadi, siap bikin video sinematik? [excited tone] Jangan lupa LIKE dan FOLLOW untuk tips lainnya. Sampai jumpa!', 'Wide shot dengan senyuman dan tangan melambai, background yang menarik.', 'Buat akhir yang ceria dan menggugah semangat', 5, '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', '2025-07-20 13:34:16.464', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cad96dd7-92c0-4d56-b209-01bae7f35339'::uuid, '11653dd9-475c-4dd4-8fb5-6615d41c349d'::uuid, 2, 'Main Content', '3-8s', 'USB-C', 'Pertama, USB-C! [informative tone] Ini adalah standar baru. Dikenal cepat, multifungsi, dan reversible! Jadi mau dipasang dari sisi mana pun, tetap bisa. Keren kan?', 'Medium shot kabel USB-C dengan highlight konektor, gentle pan untuk menunjukkan fungsionalitas...', 'Highlight key features with on-screen text', 2, '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('ffed0b28-921b-4852-9e8a-aba189721ae0'::uuid, '11653dd9-475c-4dd4-8fb5-6615d41c349d'::uuid, 3, 'Main Content', '8-13s', 'Lightning', 'Sekarang, kita bahas Lightning. [informative tone] Ini milik Apple. Juga reversible, tapi kecepatan transfer data dan daya terbatas dibandingkan USB-C. Still worth it bagi pengguna iPhone!', 'Medium shot kabel Lightning dengan efek zoom pada konektor, menonjolkan logo Apple...', 'Use comparisons to emphasize differences', 3, '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7ee98d74-c5e5-4edd-99c2-6725a60a8a60'::uuid, '11653dd9-475c-4dd4-8fb5-6615d41c349d'::uuid, 4, 'Conclusion', '13-20s', 'Mana yang kamu pilih?', 'Jadi, pilihan ada di tangan kalian! [encouraging tone] USB-C untuk kecepatan dan fleksibilitas, atau Lightning untuk iPhone kamu? Komentar di bawah ya!', 'Wide shot presenter tampil ceria dengan kedua kabel di tangan, berinteraksi langsung dengan audience...', 'End with a strong CTA to drive engagement', 4, '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', '2025-07-20 13:34:48.945', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('22831260-c301-43e8-8a52-54bd89c190ad'::uuid, 'bce52fac-f6e0-49ec-8fba-5912239f0602'::uuid, 2, 'Main Content', '3-8s', 'SHORTCUT #1', 'Pertama, gunakan CTRL + C untuk COPY dan CTRL + V untuk PASTE. Ini adalah dasar yang harus kalian kuasai! [enthusiastic]', 'Close-up tangan yang menunjukkan penggunaan shortcut di keyboard, dengan teks overlay yang menyertai.', 'Demonstrate the function visually as you speak.', 2, '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cb56dcff-f148-4c0f-90f8-d94067987ad2'::uuid, 'bce52fac-f6e0-49ec-8fba-5912239f0602'::uuid, 3, 'Main Content', '8-13s', 'SHORTCUT #2', 'Kedua, coba CTRL + Z untuk UNDO dan CTRL + Y untuk REDO. Jangan panik kalau ada yang salah! [excited]', 'Medium shot yang menggambarkan skenario kesalahan di layar, lalu kembali dengan shortcut yang tepat.', 'Use humor to lighten the topic and keep viewers engaged.', 3, '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('962a1a04-e3eb-4b2d-995a-220e9af0c004'::uuid, 'bce52fac-f6e0-49ec-8fba-5912239f0602'::uuid, 4, 'Main Content', '13-18s', 'SHORTCUT #3', 'Terakhir, gunakan ALT + TAB untuk beralih antara aplikasi. Ini sangat membantu saat multitasking! [encouraging]', 'Wide shot memperlihatkan beberapa aplikasi terbuka di layar, dengan pengguna beralih cepat antara aplikasi.', 'Show real-life application to reinforce learning.', 4, '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('203a0424-22b0-4224-b8f7-db56aae4c3fc'::uuid, 'bce52fac-f6e0-49ec-8fba-5912239f0602'::uuid, 5, 'Call to Action', '18-25s', 'LIKE & FOLLOW!', 'Nah, itu dia tips singkatnya! Jangan lupa untuk LIKE dan FOLLOW untuk lebih banyak tips produktivitas ya! [cheerful]', 'Medium shot dengan jari menunjuk ke arah kamera sambil tersenyum, menunjukkan semangat positif.', 'End with a strong call to action to engage the audience.', 5, '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', '2025-07-20 13:35:25.538', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c10dce23-434b-4b92-8fe5-832f1f0bc231'::uuid, '62c77009-1b98-4205-a2fe-ed07e50989d1'::uuid, 2, 'Main Content', '3-10s', 'UNBOXING WAKTUNYA!', 'Oke, tanpa berlama-lama, mari kita buka kotaknya! [excited tone] Pertama, lihat deh kemasannya yang SANGAT menarik dan elegan...', 'Medium shot melakukan unboxing, fokus pada detail kemasan, slow motion saat membuka kotak.', 'Highlight features while unboxing', 2, '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('90a76bdf-d817-46de-96c7-7c0918b5cec2'::uuid, '62c77009-1b98-4205-a2fe-ed07e50989d1'::uuid, 3, 'Main Content', '10-15s', 'PERTAMA KALI MENCOBA', 'Wow, lihat bentuknya! [amazed tone] Sekarang saatnya coba! Apa ANC-nya beneran berfungsi? Yuk kita cek...', 'Close-up saat mencoba earbuds di telinga, ekspresi wajah menunjukkan rasa ingin tahu.', 'Capture honest reaction during tryout', 3, '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7d9d1a61-a5fd-4aab-8586-74f536a3a7a6'::uuid, '62c77009-1b98-4205-a2fe-ed07e50989d1'::uuid, 4, 'Main Content', '15-20s', 'IMPRESSION PERTAMA', 'Hmm... [thoughtful tone] Suaranya jelas banget dan ANCI-nya terasa! Cocok banget buat kalian yang suka denger musik tanpa gangguan.', 'Medium shot duduk santai sambil mendengarkan musik, memberikan thumbs up.', 'Conclude with a positive note', 4, '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', '2025-07-20 13:36:01.159', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('58c51a66-0486-4fd5-8327-3f4b000af226'::uuid, 'ba73159c-804c-4da2-9190-82b186364480'::uuid, 2, 'Main Content', '3-8s', 'CARA KERJA', 'Jadi, guys, wireless charging itu berfungsi dengan menggunakan INDUKSI MAGNETIK! [excited tone] Charger ini menghasilkan medan magnet yang bisa mengisi baterai ponsel kamu.', 'Medium shot, menunjukkan charger wireless dan ponsel berada di atasnya, sambil menggerakkan tangan menunjukkan arus.', 'Gunakan tangan untuk menunjukkan gerakan energi', 2, '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e6adb5c6-c003-4cb2-a94c-6b6207b0bb6e'::uuid, 'ba73159c-804c-4da2-9190-82b186364480'::uuid, 3, 'Main Content', '8-15s', 'FITUR HEMAT ENERGI!', 'Keuntungan dari wireless charging adalah HEMAT ENERGI! [enthusiastic tone] Kamu tidak perlu khawatir kabel yang kusut atau rusak lagi.', 'Wide shot, menunjukkan beberapa perangkat yang diisi secara bersamaan di charger wireless.', 'Tunjukkan beberapa gadget di sekitar', 3, '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d16ceb96-9c7d-4acf-a31e-e7088e2c8741'::uuid, 'ba73159c-804c-4da2-9190-82b186364480'::uuid, 4, 'Main Content', '15-20s', 'COBA SEKARANG!', 'Jadi, sudah siap untuk coba wireless charging? [motivational tone] Ayo, ganti cara kamu mengisi baterai!', 'Extreme close-up, menunjukkan tangan mengambil ponsel dari charger wireless dengan senyuman.', 'Tutup dengan senyuman dan gerakan positif', 4, '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', '2025-07-20 13:36:36.085', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a1fc73b7-5d37-4f81-94a0-2732684bfa8b'::uuid, 'bd9963e3-b98d-45d8-ada3-b1d1c096dddb'::uuid, 2, 'Main Content', '3-10s', '1. Google Keep', 'Pertama, ada GOOGLE KEEP. Aplikasi ini super mudah digunakan, bisa buat catatan, daftar tugas, dan bahkan mencatat suara. Yang paling keren, bisa diakses di semua perangkat!', 'Medium shot dengan smartphone menampilkan aplikasi Google Keep, fingers tapping di layar.', 'Show the app interface while explaining.', 2, '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('2005b6db-a3a1-4cb7-8d9f-dcfc9c5a0ff7'::uuid, 'bd9963e3-b98d-45d8-ada3-b1d1c096dddb'::uuid, 3, 'Main Content', '10-15s', '2. Microsoft OneNote', 'Kedua, ada MICROSOFT ONENOTE. Cocok banget untuk kalian yang suka bikin catatan terorganisir dengan berbagai format. Plus, fitur syncing-nya bikin semua catatan selalu up-to-date!', 'Close-up layar laptop dengan ONENOTE dan smartphone dengan tampilan yang sama, menunjukkan sinkronisasi.', 'Highlight its organizational features.', 3, '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('5dac37c4-36af-49f0-bf8a-c36100f8792c'::uuid, 'bd9963e3-b98d-45d8-ada3-b1d1c096dddb'::uuid, 4, 'Main Content', '15-20s', '3. Evernote', 'Terakhir, EVERNOTE. Ini aplikasi yang lengkap, bisa buat catatan, menyimpan artikel, hingga gambar. Jadi, kalau kalian butuh semua di satu tempat, ini jawabannya!', 'Medium shot dengan tampilan Evernote di smartphone dan tablet, menyoroti fitur-fitur yang ada.', 'Emphasize on its versatility.', 4, '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d303cec2-80b6-460b-9097-93698e2a40d7'::uuid, 'bd9963e3-b98d-45d8-ada3-b1d1c096dddb'::uuid, 5, 'Call to Action', '20-25s', 'Coba Sekarang!', 'Nah, itu dia 3 aplikasi catatan terbaik! Coba yuk, dan share mana yang jadi favorit kalian di kolom komentar!', 'Wide shot dengan senyuman, menunjukkan smartphone dan meminta viewers untuk berinteraksi.', 'Encourage viewers to leave comments and engage.', 5, '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', '2025-07-20 13:37:09.564', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('596bc356-9cbf-4429-ba0f-a20b03453c2d'::uuid, '657c5234-1077-4849-ac4a-8e8b9475dfe3'::uuid, 2, 'Main Content', '3-10s', 'CARA BACKUP DATA', 'Pertama, pilih aplikasi cloud storage favoritmu! Kayak Google Drive atau Dropbox. Install dan buka aplikasinya.', 'Medium shot menampilkan layar smartphone dengan aplikasi cloud yang sudah dibuka, memfokuskan pada langkah-langkah yang diambil...', 'Show the installation and app interface to guide viewers.', 2, '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('fab8ed8f-e392-4afe-9e03-aecc03ce37e5'::uuid, '657c5234-1077-4849-ac4a-8e8b9475dfe3'::uuid, 3, 'Main Content', '10-15s', 'ATUR BACKUP OTOMATIS!', 'Setelah itu, atur penyimpanan otomatis! Cukup ke pengaturan, aktifkan fitur backup otomatis, dan pilih folder yang mau di-backup.', 'Close-up pada pengaturan aplikasi, memperlihatkan langkah-langkah yang harus diikuti...', 'Use screen recording to clearly show the settings.', 3, '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('74a8390f-d063-4c61-ba20-dd06db1c1d73'::uuid, '657c5234-1077-4849-ac4a-8e8b9475dfe3'::uuid, 4, 'Conclusion', '15-20s', 'SELESAI!', 'Sekarang, data pentingmu terjamin aman di cloud! Jangan lupa share video ini ke teman-temanmu!', 'Wide shot menunjukkan pengguna yang tersenyum sambil menunjukkan thumbs up, dengan latar belakang ceria...', 'End with a strong call to action for engagement.', 4, '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', '2025-07-20 13:37:44.543', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('8701d410-deeb-45e4-b912-e6dff58e560f'::uuid, 'e9e086c9-d0f1-4806-8f0e-9954f4d68d27'::uuid, 2, 'Main Content', '3-8s', 'APAKAH 50-30-20?', 'Pertama, apa itu 50-30-20? Jadi begini, GENG! 50% dari penghasilanmu untuk kebutuhan pokok, 30% untuk keinginan, dan 20% untuk ditabung.', 'Medium shot dengan tabel grafik tentang alokasi uang, pan ke kiri untuk menunjukkan bagian kebutuhan pokok.', 'Use hand gestures to emphasize points', 2, '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9be21f82-362b-419d-9be3-7a8f1165d82e'::uuid, 'e9e086c9-d0f1-4806-8f0e-9954f4d68d27'::uuid, 3, 'Main Content', '8-15s', 'BAGIAN PERTAMA!', 'Pertama, 50% untuk kebutuhan dasar seperti makanan, transportasi, dan tagihan. Pastikan ini terpenuhi terlebih dahulu! [serious tone]', 'Medium shot dengan lebih banyak detail tentang kebutuhan, menampilkan barang-barang seperti makanan, transport, dll.', 'Use relatable visuals to make it clearer', 3, '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b9197ea4-8e34-4cef-a57c-a9333f65063b'::uuid, 'e9e086c9-d0f1-4806-8f0e-9954f4d68d27'::uuid, 4, 'Main Content', '15-22s', 'BAGIAN KEDUA & KETIGA!', 'Selanjutnya, 30% untuk hal yang kalian inginkan dan 20% untuk menabung. Jadi, kembangkan gaya hidup yang sesuai ya! [excited tone]', 'Medium shot dengan sketsa hal-hal menyenangkan dan bank sebagai simbol menabung, pan ke kanan.', 'Conclude with a positive note, encouraging savings', 4, '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b6d4072c-c466-4ffd-9bff-65ea510bb299'::uuid, 'e9e086c9-d0f1-4806-8f0e-9954f4d68d27'::uuid, 5, 'Call to Action', '22-25s', 'Coba SEKARANG!', 'Coba deh terapkan 50-30-20, dan lihat perubahan keuanganmu! Jangan lupa follow untuk tips keuangan lainnya! [encouraging tone]', 'Wide shot dengan ekspresi bahagia, melambai ke kamera, pemandangan latar yang cerah.', 'End with a strong CTA and friendly engagement', 5, '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', '2025-07-20 13:38:23.331', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('2b9a6172-1b97-4a95-94ff-2a8571baf14c'::uuid, '6785cc33-38da-4aef-b0d3-7892d16368fb'::uuid, 2, 'Main Content', '3-8s', 'Saham', 'Pertama, mari kita bahas SAHAM. SAHAM adalah kepemilikan di perusahaan. Kalian bisa dapat DIVIDEN jika perusahaan untung! [excited tone] Tapi risikonya lebih tinggi.', 'Medium shot dengan grafik yang menunjukkan fluktuasi saham, menggunakan natural light...', 'Use visuals to illustrate points clearly', 2, '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('8e510264-4994-435e-a378-01d3ae9757df'::uuid, '6785cc33-38da-4aef-b0d3-7892d16368fb'::uuid, 3, 'Main Content', '8-13s', 'Reksa Dana', 'Nah, REKSA DANA itu seperti KUMPULAN SAHAM. Manajer investasi yang kelola. Jadi, lebih aman dibandingkan investasi langsung di saham! [informative tone]', 'Wide shot dengan berbagai jenis investasi di meja, termasuk gambar reksa dana...', 'Engage with the audience through eye contact', 3, '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7011fac2-8ac7-4f7c-80a0-09933365ffbd'::uuid, '6785cc33-38da-4aef-b0d3-7892d16368fb'::uuid, 4, 'Main Content', '13-20s', 'Kesimpulan', 'Jadi, jika kalian mencari keuntungan cepat, SAHAM bisa jadi pilihan. Tapi, untuk investasi jangka panjang yang lebih aman, pilihlah REKSA DANA! [encouraging tone]', 'Medium shot berbicara langsung ke kamera, dengan grafik ringkasan di samping...', 'End with a strong call to action', 4, '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', '2025-07-20 13:38:59.507', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('e54e6aa9-7843-4151-9104-800a9849a3bc'::uuid, 'c2d2cd63-e6ad-4ba0-9cbb-007dda8149bb'::uuid, 2, 'Main Content', '3-10s', 'LANGKAH 1', 'Langkah pertama, buka spreadsheet kalian. [excited tone] Buat kolom untuk PENGELUARAN dan PENDAPATAN. [pause] Ini penting untuk memisahkan semua aliran uang!', 'Screen recording dari presenter yang membuka spreadsheet dan membuat kolom-kolom tersebut.', 'Make sure to demonstrate clearly with focus on the screen.', 2, '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('6e0e9c8a-727e-491e-a0d9-69b22c2d3435'::uuid, 'c2d2cd63-e6ad-4ba0-9cbb-007dda8149bb'::uuid, 3, 'Main Content', '10-15s', 'LANGKAH 2', 'Selanjutnya, di kolom PENGELUARAN, tulis semua pengeluaran kalian. [informative tone] Misalnya, uang makan, transportasi, dan hiburan. Jangan sampai ada yang terlewat ya!', 'Close-up pada kolom pengeluaran yang diisi, dengan contoh jelas ditulis.', 'Encourage viewers to keep track of their expenses.', 3, '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('b1d6625d-3570-4856-89b6-24b8a01763a8'::uuid, 'c2d2cd63-e6ad-4ba0-9cbb-007dda8149bb'::uuid, 4, 'Main Content', '15-20s', 'LANGKAH 3', 'Terakhir, total pengeluaran dan pendapatan kalian. [excited tone] Pastikan pendapatan kalian lebih besar dari pengeluaran untuk menghindari masalah keuangan!', 'Presenter menunjukkan cara menghitung total dengan rumus spreadsheet, menampilkan hasilnya.', 'Highlight how easy it is to track finances.', 4, '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('703c5d5f-46b3-4e03-a900-91127062e27f'::uuid, 'c2d2cd63-e6ad-4ba0-9cbb-007dda8149bb'::uuid, 5, 'Call to Action', '20-25s', 'SEGERA Coba!', 'Nah, itu dia cara mudah membuat anggaran bulanan! [enthusiastic tone] Coba sekarang dan bagikan hasilnya di kolom komentar ya!', 'Presenter tersenyum dan memberikan jempol, menunjukkan spreadsheet yang sudah siap.', 'Encourage audience interaction by asking them to share.', 5, '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', '2025-07-20 13:39:39.677', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('64b90a7e-af3c-402c-b324-c625c95fefef'::uuid, '7166f4f6-cef1-4061-9f75-d2c6e97cd09e'::uuid, 2, 'Main Content', '3-10s', 'KENAPA PERLU?', 'Kenapa sih kita butuh EMERGENCY FUND? [explaining tone] Ini untuk perlindungan finansial! Misalnya, biaya medis atau kehilangan pekerjaan yang tiba-tiba.', 'Medium shot dengan gesture menunjuk ke infographic yang menjelaskan manfaat.', 'Use hand gestures to highlight key points.', 2, '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('fc2c228b-c88d-4830-837c-84ae0c1fd861'::uuid, '7166f4f6-cef1-4061-9f75-d2c6e97cd09e'::uuid, 3, 'Main Content', '10-15s', 'BAGAIMANA CARANYA?', 'Lalu, gimana cara memulainya? [encouraging tone] Mulai dengan menyisihkan 10% dari pendapatanmu setiap bulan. Gampang kan?', 'Close-up tangan menunjukkan uang dan menghitung, dengan background yang ceria.', 'Make it visually engaging with actions.', 3, '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('aad642d1-6f69-4b1e-ac19-c4e6a008dcc3'::uuid, '7166f4f6-cef1-4061-9f75-d2c6e97cd09e'::uuid, 4, 'Main Content', '15-20s', 'START NOW!', 'Ingat, setiap langkah kecil itu penting! [motivating tone] Ayo mulai EMERGENCY FUND kalian sekarang juga! Like & Share jika bermanfaat!', 'Medium shot dengan senyuman lebar, tangan mengajak untuk berinteraksi.', 'End with a strong call to action.', 4, '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', '2025-07-20 13:40:20.251', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4b6832e5-3a60-43dd-98d1-2a3b8f59ba82'::uuid, 'd9d718c8-8a6f-4ea1-b06d-618e90208e42'::uuid, 2, 'Main Content', '3-8s', 'TIP #1: PILIH APLIKASI YANG TEPAT', 'Pertama, pilih aplikasi cashback yang sudah terbukti aman dan banyak pemakai. Pastikan juga banyak merchant kerjasama, ya! Cek rating-nya.', 'Medium shot dengan tangan menunjukkan aplikasi di ponsel.', 'Tunjukkan feedback positif dari pengguna lain', 2, '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a4eb5cc2-82c3-4824-abea-f93d5345d2ae'::uuid, 'd9d718c8-8a6f-4ea1-b06d-618e90208e42'::uuid, 3, 'Main Content', '8-13s', 'TIP #2: KUMPULKAN POINT!', 'Selanjutnya, kumpulkan POINT dari setiap transaksi. Ini bisa bikin uang kembali mu semakin banyak, lho! Jangan lupa ikuti promo-promo menarik.', 'Medium shot dengan close-up aplikasi menampilkan poin yang didapat.', 'Gunakan grafik untuk menunjukkan pertambahan poin', 3, '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('2405fd55-ff1f-4579-b22a-dea67a79728a'::uuid, 'd9d718c8-8a6f-4ea1-b06d-618e90208e42'::uuid, 4, 'Main Content', '13-20s', 'TIP #3: GUNAKAN SAAT PROMO', 'Terakhir, manfaatkan momen diskon atau promo spesial! Ini saat yang tepat untuk mendapatkan cashback lebih banyak.', 'Wide shot dengan tampilan berbagai produk saat promo di aplikasi.', 'Buat suasana ceria dengan musik latar', 4, '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('cfb89a26-d9c1-4606-ae27-2864c0e954c2'::uuid, 'd9d718c8-8a6f-4ea1-b06d-618e90208e42'::uuid, 5, 'CTA', '20-25s', 'Coba sekarang!', 'Jadi, tunggu apa lagi? Mulai belanja online hemat dengan aplikasi cashback dan rasakan bedanya! Like dan share, ya!', 'Close-up wajah dengan ekspresi semangat, mengajak penonton.', 'Akhiri dengan senyuman dan gerakan tangan untuk CTA', 5, '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', '2025-07-20 13:40:50.867', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('a694f4d1-a0e4-4c9d-b2db-590695e283bc'::uuid, 'c1ecdfdd-fa39-4767-9864-7b23d51f98b6'::uuid, 2, 'Main Content', '3-8s', 'KESALAHAN #1', 'Kesalahan pertama adalah...TIDAK MEMBUAT ANGGARAN! [serious tone] Kita sering menghabiskan uang tanpa tahu ke mana perginya...', 'Medium shot dengan penjelasan di whiteboard, memperlihatkan pemasukan dan pengeluaran...', 'Tunjukkan contoh anggaran sederhana', 2, '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('8804bb94-57c3-45b8-9c17-f65adefd8671'::uuid, 'c1ecdfdd-fa39-4767-9864-7b23d51f98b6'::uuid, 3, 'Main Content', '8-15s', 'KESALAHAN #2', 'Kedua, BELANJA TANPA RENCANA! [excited tone] Kalian sering gak sih impulsif beli barang yang sebenarnya gak penting?', 'Wide shot dengan contoh barang-barang belanjaan, menunjukkan reaksi konyol saat membeli...', 'Perlihatkan perbandingan dengan dan tanpa rencana belanja', 3, '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('0eec4d47-7050-446b-9160-7f5bbdff827e'::uuid, 'c1ecdfdd-fa39-4767-9864-7b23d51f98b6'::uuid, 4, 'Main Content', '15-20s', 'KESALAHAN #3', 'Dan terakhir, MENYIMPAN UANG KURANG! [serious tone] Ingat, guys, penting banget untuk menyimpan sebagian dari penghasilan kita...', 'Close-up tangan memasukkan uang ke dalam celengan, dengan wajah penuh harapan...', 'Gunakan visual celengan yang lucu dan menarik', 4, '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', '2025-07-20 13:41:21.181', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('71307db6-c718-4b6f-9246-4f365be6bbc9'::uuid, 'ca27451b-a8ba-46e2-8bba-e75b75430b5f'::uuid, 2, 'Main Content', '3-8s', 'LANGKAH PERTAMA', 'Pertama, pilih platform yang sudah terdaftar dan memiliki reputasi baik. Pastikan keamanannya terjamin! [excited tone]', 'Medium shot dengan smartphone di tangan, menampilkan aplikasi investasi emas...', 'Tekan aplikasi di layar dengan jelas dan percaya diri', 2, '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('143555f6-aa57-487d-8600-54baae9c44e0'::uuid, 'ca27451b-a8ba-46e2-8bba-e75b75430b5f'::uuid, 3, 'Main Content', '8-13s', 'LANGKAH KEDUA', 'Kedua, pastikan ada fitur keamanan seperti autentikasi dua faktor. Ini penting! [serious tone]', 'Close-up layar smartphone menunjukkan pengaturan keamanan...', 'Tunjukkan bagaimana cara mengaktifkan fitur tersebut', 3, '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('fbb1b6fa-0d61-4d36-ae79-304f6308f1f8'::uuid, 'ca27451b-a8ba-46e2-8bba-e75b75430b5f'::uuid, 4, 'Main Content', '13-18s', 'LANGKAH KETIGA', 'Ketiga, mulailah dengan jumlah kecil dan investasi secara rutin. KONSISTENSI adalah kunci! [motivational tone]', 'Wide shot menampilkan pengguna yang dengan semangat memasukkan data investasi...', 'Gunakan gesture tangan untuk menunjukkan semangat', 4, '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', '2025-07-20 13:41:55.969', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('92a339fa-9629-485d-b1f4-bf2a5a5244a5'::uuid, '56ee3216-38e7-4442-b4fb-849d651e96cb'::uuid, 2, 'Main Content', '3-15s', 'CARA KERJA!', 'Gimana sih cara kerjanya? Pertama, siapin amplop untuk setiap kategori pengeluaran: makanan, transportasi, dan hiburan! [energetic tone] Setiap bulan, isi amplop dengan uang yang sudah kalian anggarkan!', 'Wide shot memperlihatkan meja dengan amplop yang ditandai sesuai kategori dan seseorang mengisinya.', 'Tunjukkan amplop dengan jelas dan kategori yang membuat penasaran.', 2, '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('d3019ec2-6eaf-442f-9076-ecb0f7636a5b'::uuid, '56ee3216-38e7-4442-b4fb-849d651e96cb'::uuid, 3, 'Main Content', '15-30s', 'KEUNTUNGAN!', 'Keuntungannya? Kalian jadi lebih disiplin dan tahu persis ke mana uang kalian pergi! [excited tone] Plus, ini bikin kalian lebih menghargai setiap pengeluaran!', 'Medium shot dengan ekspresi senang sambil menunjukkan jumlah uang di amplop yang tersisa.', 'Sertakan ekspresi positif saat menjelaskan manfaatnya.', 3, '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('f9a2a14c-5ad8-463d-bb75-2bde654b429c'::uuid, '56ee3216-38e7-4442-b4fb-849d651e96cb'::uuid, 4, 'Main Content', '30-45s', 'TIPS ADITIONAL!', 'Tips tambahan, jangan lupa review pengeluaran kalian tiap bulan! [enthusiastic tone] Ini akan bantu kalian untuk lebih baik di bulan selanjutnya!', 'Close-up tangan yang mencatat pengeluaran di buku catatan, dengan amplop di latar belakang.', 'Tunjukkan proses review dengan jelas.', 4, '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('9de2b95b-6090-4f99-b4dd-8edeadbcf6a7'::uuid, '56ee3216-38e7-4442-b4fb-849d651e96cb'::uuid, 5, 'Call to Action', '45-60s', 'IKUTIN KALAU BERMANFAAT!', 'Yuk, cobain BUDGETING ALA AMPLOP dan rasakan bedanya! Jangan lupa follow untuk tips keuangan lainnya! [friendly tone]', 'Wide shot dengan thumbs up dan senyuman, serta amplop yang terlihat jelas.', 'Akhiri dengan interaksi yang positif dan ajakan untuk follow.', 5, '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', '2025-07-20 13:42:27.022', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4293c31a-a6a5-4db3-93e6-3feb6bb7afe5'::uuid, '098304a2-a8f2-40fb-8322-fea897f57848'::uuid, 2, 'Main Content', '3-10s', 'APA ITU BUNGA MAJEMUK?', 'Oke, jadi apa sih BUNGA MAJEMUK itu? [informative tone] Ini adalah cara di mana bunga dihasilkan tidak hanya dari modal awal, tapi juga dari bunga yang sudah ada sebelumnya! Ini yang bikin jumlah uang bertambah lebih cepat.', 'Medium shot dengan diagram bunga majemuk yang menjelaskan prosesnya dengan animasi.', 'Utilize visuals to make complex ideas simpler.', 2, '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4a697725-a96b-47b5-a692-37def67ae32d'::uuid, '098304a2-a8f2-40fb-8322-fea897f57848'::uuid, 3, 'Main Content', '10-15s', 'CONTOH NYA!', 'Misalnya, jika kamu menabung Rp1.000.000 dengan bunga 5% per tahun, setelah 10 tahun, kamu bisa menikmati Rp1.628.894! [excited tone] Itu berkat efek BUNGA MAJEMUK ini.', 'Close-up pada kalkulator dengan angka yang muncul secara dramatis, serta grafik pertumbuhan.', 'Show concrete examples and calculations to keep viewers engaged.', 3, '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('c6d2353a-1804-433c-a622-fd161c29b0be'::uuid, '098304a2-a8f2-40fb-8322-fea897f57848'::uuid, 4, 'Call to Action', '15-20s', 'CARA MENDAPATKAN!', 'Jadi, sekarang saatnya kamu mulai investasi! [motivational tone] Jangan sia-siakan waktu, mulai dengan BUNGA MAJEMUK, dan lihatlah uangmu tumbuh! Jangan lupa LIKE dan FOLLOW untuk tips lebih banyak!', 'Wide shot dengan pembicara menunjuk ke kamera, background cerah dan penuh semangat.', 'End with a motivational call to action to encourage interaction.', 4, '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', '2025-07-20 13:43:00.713', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('f6ea0c9b-d42e-4570-b282-f4a0e55a131a'::uuid, 'e004d6d6-e2ef-43b0-9508-c0594cacb4b1'::uuid, 2, 'Main Content', '3-8s', 'APA ITU SNOWBALL?', 'Strategi SNOWBALL adalah cara melunasi utang dengan memprioritaskan utang terkecil dulu! [excited] Ini akan memberi motivasi!', 'Wide shot dengan papan tulis, menggambar siklus utang, bisa tunjukkan dua contoh utang.', 'Create a visual demo of debt prioritization.', 2, '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('4d4263c1-102d-474a-82a6-5288884ce6a8'::uuid, 'e004d6d6-e2ef-43b0-9508-c0594cacb4b1'::uuid, 3, 'Main Content', '8-15s', 'LANGKAH PERTAMA', 'Langkah pertama, LISTING semua utang kalian! [serious tone] Tuliskan total utang, suku bunga, dan bayar minimal setiap bulan.', 'Medium shot dekat dengan kertas dan pensil, menunjukkan penulisan daftar utang.', 'Engage viewers by asking them to share their debts in the comments.', 3, '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', NULL);
        INSERT INTO scenes
        (id, training_pair_id, scene_number, scene_type, "timestamp", text_overlay, voiceover, visual, tip, order_index, created_at, created_by, updated_at, updated_by, deleted_at)
        VALUES('7961656e-ce15-4a6f-8c1b-52351db17f2a'::uuid, 'e004d6d6-e2ef-43b0-9508-c0594cacb4b1'::uuid, 4, 'Main Content', '15-20s', 'JADIKAN SNOWBALL!', 'Setelah itu, fokus bayar utang terkecil! [excited] Setiap kali lunas, gunakan uangnya untuk bayar utang selanjutnya! Keren kan?', 'Medium shot dengan ekspresi semangat, tunjukkan contoh bagaimana uang sisa dipakai untuk utang lain.', 'Use enthusiastic gestures to inspire action.', 4, '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', '2025-07-20 13:43:36.143', 'SCRIPT_AGENT', NULL);
               
    ''')


def downgrade() -> None:
    op.execute('''
        DELETE FROM scenes;
        DELETE FROM hook_variants;
        DELETE FROM training_pairs;
    ''')
