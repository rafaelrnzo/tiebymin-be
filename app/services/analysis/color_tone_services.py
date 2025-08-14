import numpy as np
from PIL import Image
import io
import cv2
import mediapipe as mp
import math

class ColorToneService:
    def __init__(self):
        self.SKIN_PALETTE = {
            "Light Spring": (255, 219, 172),    
            "True Spring": (240, 184, 160),     
            "Warm Spring": (222, 169, 143),     
            "Light Summer": (250, 215, 187),    
            "True Summer": (235, 200, 175),     
            "Soft Summer": (225, 190, 165),     
            "Soft Autumn": (210, 170, 140),     
            "True Autumn": (195, 155, 125),     
            "Deep Autumn": (180, 140, 110),     
            "Deep Winter": (200, 160, 135),     
            "True Winter": (215, 175, 150),     
            "Cool Winter": (230, 190, 165)      
        }

        self.EYE_PALETTE = {
            "Light Spring": (135, 120, 85),     
            "True Spring": (100, 85, 50),       
            "Warm Spring": (85, 70, 40),        
            "Light Summer": (140, 145, 150),    
            "True Summer": (110, 115, 125),     
            "Soft Summer": (120, 125, 130),     
            "Soft Autumn": (95, 85, 70),        
            "True Autumn": (80, 65, 45),        
            "Deep Autumn": (65, 50, 35),        
            "Deep Winter": (45, 55, 70),        
            "True Winter": (60, 70, 85),        
            "Cool Winter": (75, 85, 100)        
        }
        
        self.SEASON_CHARACTERISTICS = {
            "Light Spring": {"warmth": 0.7, "clarity": 0.8, "depth": 0.3},
            "True Spring": {"warmth": 0.8, "clarity": 0.9, "depth": 0.5},
            "Warm Spring": {"warmth": 0.9, "clarity": 0.7, "depth": 0.6},
            "Light Summer": {"warmth": 0.2, "clarity": 0.7, "depth": 0.3},
            "True Summer": {"warmth": 0.1, "clarity": 0.8, "depth": 0.5},
            "Soft Summer": {"warmth": 0.3, "clarity": 0.4, "depth": 0.4},
            "Soft Autumn": {"warmth": 0.6, "clarity": 0.4, "depth": 0.6},
            "True Autumn": {"warmth": 0.8, "clarity": 0.6, "depth": 0.7},
            "Deep Autumn": {"warmth": 0.7, "clarity": 0.7, "depth": 0.9},
            "Deep Winter": {"warmth": 0.1, "clarity": 0.8, "depth": 0.9},
            "True Winter": {"warmth": 0.0, "clarity": 0.9, "depth": 0.7},
            "Cool Winter": {"warmth": 0.0, "clarity": 0.8, "depth": 0.5}
        }

    def _color_distance(self, rgb1, rgb2):
        r1, g1, b1 = rgb1
        r2, g2, b2 = rgb2
        return math.sqrt(2*(r1-r2)**2 + 4*(g1-g2)**2 + 3*(b1-b2)**2)

    def _calculate_warmth(self, rgb):
        r, g, b = rgb
        warmth = (r + g - 2*b) / (r + g + b + 1)
        return max(0, min(1, (warmth + 1) / 2))

    def _calculate_clarity(self, rgb, contrast):
        r, g, b = rgb
        saturation = (max(r, g, b) - min(r, g, b)) / (max(r, g, b) + 1)
        clarity = (saturation * 0.7 + contrast / 100 * 0.3)
        return max(0, min(1, clarity))

    def _calculate_depth(self, rgb, hair_rgb, eye_rgb):
        skin_lab = cv2.cvtColor(np.uint8([[rgb]]), cv2.COLOR_RGB2LAB)[0][0]
        hair_lab = cv2.cvtColor(np.uint8([[hair_rgb]]), cv2.COLOR_RGB2LAB)[0][0]
        eye_lab = cv2.cvtColor(np.uint8([[eye_rgb]]), cv2.COLOR_RGB2LAB)[0][0]
        
        avg_lightness = (skin_lab[0] + hair_lab[0] + eye_lab[0]) / 3
        depth = 1 - (avg_lightness / 100) 
        return max(0, min(1, depth))

    def _enhanced_seasonal_classification(self, skin_rgb, eye_rgb, hair_rgb, facial_contrast):
        warmth = self._calculate_warmth(skin_rgb)
        clarity = self._calculate_clarity(skin_rgb, facial_contrast)
        depth = self._calculate_depth(skin_rgb, hair_rgb, eye_rgb)
        
        best_match = None
        best_score = float('inf')
        
        for season, characteristics in self.SEASON_CHARACTERISTICS.items():
            warmth_diff = abs(warmth - characteristics["warmth"])
            clarity_diff = abs(clarity - characteristics["clarity"])
            depth_diff = abs(depth - characteristics["depth"])
            
            skin_distance = self._color_distance(skin_rgb, self.SKIN_PALETTE[season])
            
            score = (
                warmth_diff * 0.3 +
                clarity_diff * 0.2 +
                depth_diff * 0.2 +
                (skin_distance / 255) * 0.3 
            )
            
            if score < best_score:
                best_score = score
                best_match = season
                
        return best_match

    def _categorize_color(self, rgb, palette):
        return min(palette, key=lambda k: self._color_distance(rgb, palette[k]))

    def _average_rgb(self, image, mask=None):
        if mask is not None:
            pixels = image[mask]
        else:
            pixels = image.reshape(-1, 3)
        
        if pixels.size == 0:
            return (0, 0, 0)
            
        if len(pixels) > 10:
            mean_pixel = np.mean(pixels, axis=0)
            std_pixel = np.std(pixels, axis=0)
            mask_outliers = np.all(np.abs(pixels - mean_pixel) <= 2 * std_pixel, axis=1)
            if np.any(mask_outliers):
                pixels = pixels[mask_outliers]
        
        return tuple(int(x) for x in np.mean(pixels, axis=0))

    def _get_enhanced_skin_mask(self, image):
        ycbcr = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
        cb = ycbcr[:, :, 2]
        cr = ycbcr[:, :, 1]
        mask1 = (cb >= 85) & (cb <= 135) & (cr >= 135) & (cr <= 180)
        
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        h, s, v = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]
        mask2 = ((h >= 0) & (h <= 20) | (h >= 160) & (h <= 180)) & (s >= 15) & (s <= 170) & (v >= 60)
        
        combined_mask = mask1 | mask2
        
        kernel = np.ones((3, 3), np.uint8)
        combined_mask = cv2.morphologyEx(combined_mask.astype(np.uint8), cv2.MORPH_CLOSE, kernel)
        combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)
        
        return combined_mask.astype(bool)

    def _get_eye_color(self, image, landmarks, eye_indices):
        if not landmarks or len(eye_indices) < 4:
            return (90, 90, 90) 
            
        points = []
        for i in eye_indices:
            if i < len(landmarks):
                x = int(landmarks[i].x * image.shape[1])
                y = int(landmarks[i].y * image.shape[0])
                x = max(0, min(x, image.shape[1] - 1))
                y = max(0, min(y, image.shape[0] - 1))
                points.append((x, y))
        
        if len(points) < 3:
            return (90, 90, 90)
            
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(points, dtype=np.int32)], 255)
        
        eye_center = np.mean(points, axis=0).astype(int)
        iris_radius = int(np.linalg.norm(np.array(points[0]) - np.array(points[2])) / 4)
        cv2.circle(mask, tuple(eye_center), iris_radius, 255, -1)
        
        return self._average_rgb(image, mask == 255)

    def _get_hair_color(self, image, face_bbox):
        x, y, w, h = face_bbox
        
        hair_height = int(0.6 * h) 
        hair_y_start = max(0, y - hair_height)
        hair_y_end = max(0, y - int(0.1 * h))  
        
        regions = []
        
        if hair_y_start < hair_y_end:
            top_hair = image[hair_y_start:hair_y_end, x:x + w]
            if top_hair.size > 0:
                regions.append(top_hair)
        
        temple_width = int(0.3 * w)
        temple_height = int(0.4 * h)
        
        left_temple = image[y:y + temple_height, max(0, x - temple_width):x]
        if left_temple.size > 0:
            regions.append(left_temple)
            
        right_temple = image[y:y + temple_height, x + w:x + w + temple_width]
        if right_temple.size > 0 and x + w + temple_width < image.shape[1]:
            regions.append(right_temple)
        
        if not regions:
            return (100, 70, 50) 
        
        all_colors = []
        for region in regions:
            region_color = self._average_rgb(region)
            if sum(region_color) > 30: 
                all_colors.append(region_color)
        
        if not all_colors:
            return (100, 70, 50)
            
        return tuple(int(np.mean([c[i] for c in all_colors])) for i in range(3))

    def detect(self, image_bytes: bytes) -> dict:
        try:
            image_pil = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            image_cv = np.array(image_pil)
        except Exception as e:
            raise ValueError(f"Gagal membaca gambar. Error: {e}")

        mp_face_detection = mp.solutions.face_detection
        mp_face_mesh = mp.solutions.face_mesh

        with mp_face_detection.FaceDetection(
            model_selection=1, 
            min_detection_confidence=0.5
        ) as face_detection, \
             mp_face_mesh.FaceMesh(
                 static_image_mode=True, 
                 max_num_faces=1, 
                 refine_landmarks=True,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5
             ) as face_mesh:

            detection_result = face_detection.process(image_cv)
            if not detection_result.detections:
                raise ValueError("Wajah tidak terdeteksi dalam gambar.")

            bbox = detection_result.detections[0].location_data.relative_bounding_box
            ih, iw, _ = image_cv.shape
            x, y = int(bbox.xmin * iw), int(bbox.ymin * ih)
            w, h = int(bbox.width * iw), int(bbox.height * ih)

            padding = max(10, min(30, int(0.1 * min(w, h))))
            x, y = max(0, x - padding), max(0, y - padding)
            w = min(iw - x, w + padding * 2)
            h = min(ih - y, h + padding * 2)
            
            face_crop = image_cv[y:y + h, x:x + w]
            if face_crop.size == 0:
                raise ValueError("Crop wajah tidak valid.")

            skin_mask = self._get_enhanced_skin_mask(face_crop)
            avg_skin_rgb = self._average_rgb(face_crop, skin_mask)

            mesh_results = face_mesh.process(image_cv)
            avg_eye_rgb = (90, 90, 90)  # Default
            
            if mesh_results.multi_face_landmarks:
                landmarks = mesh_results.multi_face_landmarks[0].landmark
                
                right_eye_indices = [469, 470, 471, 472]  # Right eye iris area
                left_eye_indices = [474, 475, 476, 477]   # Left eye iris area
                
                eye_colors = []
                for eye_indices in [right_eye_indices, left_eye_indices]:
                    eye_color = self._get_eye_color(image_cv, landmarks, eye_indices)
                    if sum(eye_color) > 0:  # Valid color detected
                        eye_colors.append(eye_color)
                
                if eye_colors:
                    avg_eye_rgb = tuple(int(np.mean([c[i] for c in eye_colors])) for i in range(3))

            avg_hair_rgb = self._get_hair_color(image_cv, (x, y, w, h))

            skin_l = cv2.cvtColor(np.uint8([[avg_skin_rgb]]), cv2.COLOR_RGB2LAB)[0][0][0]
            hair_l = cv2.cvtColor(np.uint8([[avg_hair_rgb]]), cv2.COLOR_RGB2LAB)[0][0][0]
            eye_l = cv2.cvtColor(np.uint8([[avg_eye_rgb]]), cv2.COLOR_RGB2LAB)[0][0][0]
            
            skin_hair_contrast = abs(float(skin_l) - float(hair_l))
            skin_eye_contrast = abs(float(skin_l) - float(eye_l))
            facial_contrast = skin_hair_contrast + skin_eye_contrast

            try:
                category = self._enhanced_seasonal_classification(
                    avg_skin_rgb, avg_eye_rgb, avg_hair_rgb, facial_contrast
                )
            except:
                category = self._categorize_color(avg_skin_rgb, self.SKIN_PALETTE)

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
    
        raise ValueError("Tidak ada wajah yang terdeteksi dalam gambar.")