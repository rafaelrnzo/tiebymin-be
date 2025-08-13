import numpy as np
from PIL import Image
import io
import cv2
import mediapipe as mp
import math

class ColorToneService:
    def __init__(self):
        # Palet warna referensi (bisa dituning lagi)
        self.SKIN_PALETTE = {
            "Light Spring": (255, 230, 210),
            "True Spring": (250, 220, 190),
            "Warm Spring": (245, 210, 175),
            "Light Summer": (240, 225, 215),
            "True Summer": (235, 215, 200),
            "Soft Summer": (225, 205, 190),
            "Soft Autumn": (230, 200, 170),
            "True Autumn": (220, 190, 150),
            "Deep Autumn": (200, 160, 120),
            "Deep Winter": (210, 180, 170),
            "True Winter": (230, 200, 190),
            "Cool Winter": (220, 200, 195)
        }

    def _color_distance(self, rgb1, rgb2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)))

    def _categorize_color(self, rgb):
        return min(self.SKIN_PALETTE, key=lambda k: self._color_distance(rgb, self.SKIN_PALETTE[k]))

    def _average_rgb(self, image, mask=None):
        if mask is not None:
            pixels = image[mask]
        else:
            pixels = image.reshape(-1, 3)
        if pixels.size == 0:
            return (0, 0, 0)
        return tuple(int(x) for x in np.mean(pixels, axis=0))

    def _get_eye_color(self, image, landmarks, eye_indices):
        points = [(int(landmarks[i].x * image.shape[1]), int(landmarks[i].y * image.shape[0])) for i in eye_indices]
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(points, dtype=np.int32)], 255)
        return self._average_rgb(image, mask == 255)

    def _get_hair_color(self, image, face_bbox):
        # Ambil area di atas bounding box wajah sebagai rambut
        x, y, w, h = face_bbox
        hair_y_end = max(0, y - int(0.4 * h))
        hair_crop = image[max(0, hair_y_end - h):hair_y_end, x:x + w]
        return self._average_rgb(hair_crop)

    def detect(self, image_bytes: bytes) -> dict:
        try:
            image_pil = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            image_cv = np.array(image_pil)
        except Exception as e:
            raise ValueError(f"Gagal membaca gambar. Error: {e}")

        mp_face_detection = mp.solutions.face_detection
        mp_face_mesh = mp.solutions.face_mesh

        with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection, \
             mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True) as face_mesh:

            # Deteksi wajah
            detection_result = face_detection.process(image_cv)
            if not detection_result.detections:
                raise ValueError("Wajah tidak terdeteksi dalam gambar.")

            bbox = detection_result.detections[0].location_data.relative_bounding_box
            ih, iw, _ = image_cv.shape
            x, y = int(bbox.xmin * iw), int(bbox.ymin * ih)
            w, h = int(bbox.width * iw), int(bbox.height * ih)

            # Tambahkan padding
            padding = 20
            x, y = max(0, x - padding), max(0, y - padding)
            w, h = w + padding * 2, h + padding * 2
            face_crop = image_cv[y:y + h, x:x + w]

            if face_crop.size == 0:
                raise ValueError("Crop wajah tidak valid.")

            # Mask kulit dengan YCbCr
            ycbcr = cv2.cvtColor(face_crop, cv2.COLOR_RGB2YCrCb)
            cb = ycbcr[:, :, 2]
            cr = ycbcr[:, :, 1]
            mask = (cb >= 85) & (cb <= 135) & (cr >= 135) & (cr <= 180)
            avg_skin_rgb = self._average_rgb(face_crop, mask)

            # Deteksi face mesh untuk mata
            mesh_results = face_mesh.process(image_cv)
            avg_eye_rgb = (0, 0, 0)
            if mesh_results.multi_face_landmarks:
                landmarks = mesh_results.multi_face_landmarks[0].landmark
                # Index landmark iris kanan & kiri (Mediapipe iris indices)
                right_eye_indices = list(range(474, 478))
                left_eye_indices = list(range(469, 473))
                eye_colors = []
                for eye in [right_eye_indices, left_eye_indices]:
                    eye_colors.append(self._get_eye_color(image_cv, landmarks, eye))
                avg_eye_rgb = tuple(int(np.mean([c[i] for c in eye_colors])) for i in range(3))

            # Deteksi warna rambut
            avg_hair_rgb = self._get_hair_color(image_cv, (x, y, w, h))

            # Hitung kontras wajah
            skin_l = np.mean(cv2.cvtColor(np.uint8([[avg_skin_rgb]]), cv2.COLOR_RGB2LAB)[:, :, 0])
            hair_l = np.mean(cv2.cvtColor(np.uint8([[avg_hair_rgb]]), cv2.COLOR_RGB2LAB)[:, :, 0])
            eye_l = np.mean(cv2.cvtColor(np.uint8([[avg_eye_rgb]]), cv2.COLOR_RGB2LAB)[:, :, 0])
            facial_contrast = abs(skin_l - hair_l) + abs(skin_l - eye_l)

            # Kategorisasi
            category = self._categorize_color(avg_skin_rgb)

            return {
                "category": category,
                "average_rgb": {
                    "r": avg_skin_rgb[0],
                    "g": avg_skin_rgb[1],
                    "b": avg_skin_rgb[2]
                },
                "indicators": {
                    "skin_rgb": avg_skin_rgb,
                    "eye_rgb": avg_eye_rgb,
                    "hair_rgb": avg_hair_rgb,
                    "facial_contrast": round(float(facial_contrast), 2)
                }
            }
