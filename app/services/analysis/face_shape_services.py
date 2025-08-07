# File: services/analysis/face_shape_service.py

from transformers import ViTImageProcessor, TFSwiftFormerForImageClassification
from PIL import Image
import numpy as np
import tensorflow as tf
import os
import io

class FaceShapeService:
    def __init__(self, model_path: str):
        self.MODEL_PATH = model_path
        self.CLASS_NAMES = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']

        if not os.path.isdir(self.MODEL_PATH):
            raise RuntimeError(f"Direktori model tidak ditemukan di: {self.MODEL_PATH}")

        try:
            print(f"Memuat model dari {self.MODEL_PATH}...")
            self.processor = ViTImageProcessor.from_pretrained(self.MODEL_PATH)
            self.model = TFSwiftFormerForImageClassification.from_pretrained(self.MODEL_PATH)
            print("Model dan processor berhasil dimuat. ✅")
        except Exception as e:
            raise RuntimeError(f"Gagal memuat model atau processor. Error: {e}")

    def predict(self, image_bytes: bytes) -> dict:
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        inputs = self.processor(images=img, return_tensors="np")
        predictions = self.model.predict(inputs.pixel_values)
        probabilities = tf.nn.softmax(predictions.logits, axis=-1).numpy()[0]

        predicted_index = int(np.argmax(probabilities))  # Fix here
        predicted_label = self.CLASS_NAMES[predicted_index]
        confidence = float(probabilities[predicted_index])

        return {
            "label": predicted_label,
            "confidence": round(confidence, 4)
        }

        
from dotenv import load_dotenv
load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")
face_shape_service = FaceShapeService(model_path=MODEL_PATH)