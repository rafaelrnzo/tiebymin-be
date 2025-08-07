# File: services/analysis/face_shape_service.py

from transformers import ViTImageProcessor, TFSwiftFormerForImageClassification
from PIL import Image
import numpy as np
import tensorflow as tf
import os
import io

class FaceShapeService:
    """
    Service ini menangani klasifikasi bentuk wajah.
    Service ini memuat model dan processor sekali saja dan menyediakan metode prediksi.
    """
    def __init__(self, model_path: str):
        # Mendefinisikan konstanta dan path model
        self.MODEL_PATH = model_path
        self.CLASS_NAMES = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']

        # Memvalidasi bahwa direktori model ada
        if not os.path.isdir(self.MODEL_PATH):
            raise RuntimeError(f"Direktori model tidak ditemukan di: {self.MODEL_PATH}")

        # Memuat model dan processor saat inisialisasi
        try:
            print(f"Memuat model dari {self.MODEL_PATH}...")
            self.processor = ViTImageProcessor.from_pretrained(self.MODEL_PATH)
            self.model = TFSwiftFormerForImageClassification.from_pretrained(self.MODEL_PATH)
            print("Model dan processor berhasil dimuat. ✅")
        except Exception as e:
            raise RuntimeError(f"Gagal memuat model atau processor. Error: {e}")

    def predict(self, image_bytes: bytes) -> dict:
        """
        Memprediksi bentuk wajah dari data bytes gambar.

        Args:
            image_bytes (bytes): Konten byte dari file gambar.

        Returns:
            dict: Sebuah dictionary berisi label prediksi dan skor kepercayaan (confidence).
        """
        # Membuka gambar dari bytes dan memastikannya dalam format RGB
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # Memproses gambar menggunakan processor yang sudah dimuat
        inputs = self.processor(images=img, return_tensors="np")
        
        # Mendapatkan prediksi dari model
        predictions = self.model.predict(inputs.pixel_values)

        # Menghitung probabilitas menggunakan softmax
        probabilities = tf.nn.softmax(predictions.logits, axis=-1).numpy()[0]
        
        # Mendapatkan indeks probabilitas tertinggi
        predicted_index = np.argmax(probabilities)
        
        predicted_label = self.CLASS_NAMES[predicted_index]
        confidence = float(probabilities[predicted_index])

        return {
            "label": predicted_label,
            "confidence": round(confidence, 4)
        }

# --- PEMBUATAN SATU INSTANSI (SINGLETON) ---
# Membuat satu instansi dari service yang akan diimpor oleh bagian lain dari aplikasi.
# Ini memastikan model yang berat hanya dimuat SATU KALI saat aplikasi dimulai.
MODEL_PATH = "/Users/rafaelrnzo/Proj/Proj/Lantech/tiebymin-be/tiebymin-be-v1/swiftformer"
face_shape_service = FaceShapeService(model_path=MODEL_PATH)