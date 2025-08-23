import uuid
from typing import Optional
from repositories.celebrity_repository import CelebrityRepository

class CelebrityMatchService:
    def __init__(self, celebrity_repo: CelebrityRepository):
        self.repo = celebrity_repo

    def find_celebrity_match_id(
        self, face_shape_id: uuid.UUID, color_analysis_id: uuid.UUID
    ) -> Optional[uuid.UUID]:
        return self.repo.find_id_by_match(face_shape_id, color_analysis_id)