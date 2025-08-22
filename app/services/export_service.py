import json
from datetime import datetime
from app.models.training import TrainingPair
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

async def export_training_jsonl(output_path: str, db_session):
    result = await db_session.execute(
        select(TrainingPair)
        .where(TrainingPair.status == "APPROVED")
        .options(
            selectinload(TrainingPair.hook_variants),
            selectinload(TrainingPair.scenes),
            selectinload(TrainingPair.hashtags)
        )
    )
    training_pairs = result.unique().scalars().all()

    with open(output_path, "w", encoding="utf-8") as f:
        for tp in training_pairs:
            hooks = []
            for idx, hook in enumerate(tp.hook_variants, 1):
                hooks.append({
                    "hook_variant": hook.hook_variant or idx,
                    "scene_number": hook.scene_number or 1,
                    "scene_type": hook.scene_type or "Hook",
                    "timestamp": hook.timestamp or "0-3s",
                    "text_overlay": hook.text_overlay or "",
                    "voiceover": hook.voiceover or "",
                    "visual": hook.visual or "",
                    "tip": hook.tip or ""
                })
            script_body = []
            for idx, scene in enumerate(tp.scenes, 2):
                script_body.append({
                    "scene_number": scene.scene_number or idx,
                    "scene_type": scene.scene_type or "Main Content",
                    "timestamp": scene.timestamp or "",
                    "text_overlay": scene.text_overlay or "",
                    "voiceover": scene.voiceover or "",
                    "visual": scene.visual or "",
                    "tip": scene.tip or ""
                })
            # Updated to use hashtag string directly instead of hashtag.name
            trending_elements = [h.hashtag for h in tp.hashtags] if tp.hashtags else []

            assistant_content = {
                "type": "video_script",
                "generated_at": tp.updated_at.isoformat() if tp.updated_at else datetime.utcnow().isoformat(),
                "duration_estimate": f"{tp.duration_seconds-2}-{tp.duration_seconds+2}s" if tp.duration_seconds else "",
                "performance_score": tp.score or 0,
                "target_audience": tp.target_audience or "",
                "content_style": tp.content_style or "",
                "trending_elements": trending_elements,
                "primary_keyword": tp.topic or "",
                "data": {
                    "hooks": hooks,
                    "script_body": script_body
                }
            }

            messages = [
                {"role": "system", "content": tp.system_prompt or ""},
                {"role": "user", "content": tp.user_prompt or ""},
                {"role": "assistant", "content": json.dumps(assistant_content, ensure_ascii=False, indent=2)}
            ]

            f.write(json.dumps({"messages": messages}, ensure_ascii=False) + "\n") 