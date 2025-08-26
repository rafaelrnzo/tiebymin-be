import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import cv2
from typing import Tuple, Dict, Any
from dotenv import load_dotenv
import os 

load_dotenv()
class FaceLandmarkService:
    landmark_model_path = os.getenv("MODEL_LANDMARK_PATH")
    def __init__(self, model_path=landmark_model_path):
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            output_face_blendshapes=True,
            output_facial_transformation_matrixes=True,
            num_faces=1
        )
        self.detector = vision.FaceLandmarker.create_from_options(options)

    def _draw_landmarks_glow(self, rgb_image: np.ndarray, detection_result, line_color: Tuple[int, int, int] = (210, 77, 255), glow_intensity: int = 15, alpha: float = 0.6) -> np.ndarray:
        face_landmarks_list = detection_result.face_landmarks
        base_img = np.copy(rgb_image)
        overlay = np.zeros_like(base_img, dtype=np.uint8)
        spec = mp.solutions.drawing_utils.DrawingSpec(color=line_color, thickness=1)

        for face_landmarks in face_landmarks_list:
            face_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            face_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=lm.x, y=lm.y, z=lm.z) for lm in face_landmarks
            ])

            connections = mp.solutions.face_mesh.FACEMESH_TESSELATION
            mp.solutions.drawing_utils.draw_landmarks(overlay, face_landmarks_proto, connections, None, connection_drawing_spec=spec)
            
            connections = mp.solutions.face_mesh.FACEMESH_CONTOURS
            mp.solutions.drawing_utils.draw_landmarks(overlay, face_landmarks_proto, connections, None, connection_drawing_spec=spec)
            
            connections = mp.solutions.face_mesh.FACEMESH_IRISES
            mp.solutions.drawing_utils.draw_landmarks(overlay, face_landmarks_proto, connections, None, connection_drawing_spec=spec)

        glow = cv2.GaussianBlur(overlay, (0, 0), glow_intensity)
        glow_img = cv2.addWeighted(base_img, 1, glow, alpha, 0)
        final_img = cv2.addWeighted(glow_img, 1, overlay, 1, 0)

        return final_img

    def analyze_and_annotate(self, image_bytes: bytes) -> Tuple[bytes, Dict[str, Any]]:
        nparr = np.frombuffer(image_bytes, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img_rgb = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
        detection_result = self.detector.detect(mp_image)

        annotated_image_rgb = self._draw_landmarks_glow(img_rgb, detection_result)
        annotated_image_bgr = cv2.cvtColor(annotated_image_rgb, cv2.COLOR_RGB2BGR)
        
        success, image_buffer = cv2.imencode(".png", annotated_image_bgr)
        if not success:
            raise RuntimeError("Failed to encode annotated image to PNG format.")
        
        blendshapes_data = []
        if detection_result.face_blendshapes:
            for category in detection_result.face_blendshapes[0]:
                blendshapes_data.append({"category_name": category.category_name, "score": category.score})

        return image_buffer.tobytes(), {"blendshapes": blendshapes_data}

face_landmark_service = FaceLandmarkService()