import numpy as np
from PIL import Image
import io
import cv2
import mediapipe as mp
import math


class ColorToneService:
    def __init__(self):
        self.SKIN_PALETTE = {
            "Winter": (241, 212, 202),
            "Summer": (240, 201, 183),
            "Spring": (255, 224, 196),
            "Autumn": (234, 193, 153)
        }

    def _color_distance(self, rgb1, rgb2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)))

    def _categorize_color(self, rgb):
        return min(self.SKIN_PALETTE, key=lambda k: self._color_distance(rgb, self.SKIN_PALETTE[k]))

    def detect(self, image_bytes: bytes) -> dict:
        try:
            image_pil = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            image_cv = np.array(image_pil)
        except Exception as e:
            raise ValueError(f"Gagal membaca gambar. Error: {e}")

        with mp.solutions.face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
            result = face_detection.process(image_cv)

            if not result.detections:
                raise ValueError("Wajah tidak terdeteksi dalam gambar.")

            bbox = result.detections[0].location_data.relative_bounding_box
            ih, iw, _ = image_cv.shape
            x, y = int(bbox.xmin * iw), int(bbox.ymin * ih)
            w, h = int(bbox.width * iw), int(bbox.height * ih)

            # Tambahkan padding agar cropping tidak terlalu ketat
            padding = 20
            x, y = max(0, x - padding), max(0, y - padding)
            w, h = w + padding * 2, h + padding * 2

            face_crop = image_cv[y:y + h, x:x + w]
            if face_crop.size == 0:
                raise ValueError("Crop wajah tidak valid.")

            ycbcr = Image.fromarray(face_crop).convert('YCbCr')
            ycbcr_np = np.array(ycbcr)

            cb = ycbcr_np[:, :, 1]
            cr = ycbcr_np[:, :, 2]
            mask = (cb >= 85) & (cb <= 135) & (cr >= 135) & (cr <= 180)

            if np.sum(mask) == 0:
                raise ValueError("Tidak ada area kulit yang terdeteksi di wajah.")

            rgb_pixels = face_crop[mask]
            avg_rgb = tuple(int(x) for x in np.mean(rgb_pixels, axis=0))  # konversi ke native int

            category = self._categorize_color(avg_rgb)

            return {
                "category": category,
                "average_rgb": {
                    "r": avg_rgb[0],
                    "g": avg_rgb[1],
                    "b": avg_rgb[2]
                }
            }
