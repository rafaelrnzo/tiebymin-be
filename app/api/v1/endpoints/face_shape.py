from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from transformers import ViTImageProcessor, TFSwiftFormerForImageClassification
from PIL import Image
import numpy as np
import tensorflow as tf
import tempfile
import os
import io

router = APIRouter(
    prefix="/face-shape",
    tags=["Face Shape Classification"]
)

MODEL_PATH = "/Users/rafaelrnzo/Proj/Proj/Lantech/tiebymin-be/tiebymin-be-v1/swiftformer"
CLASS_NAMES = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']

if not os.path.isdir(MODEL_PATH):
    raise RuntimeError(f"Direktori model tidak ditemukan di: {MODEL_PATH}")

try:
    processor = ViTImageProcessor.from_pretrained(MODEL_PATH)
    model = TFSwiftFormerForImageClassification.from_pretrained(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Gagal memuat model atau processor dari {MODEL_PATH}. Error: {e}")


def predict_image(image_bytes: bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    inputs = processor(images=img, return_tensors="np")
    predictions = model.predict(inputs)

    predicted_index = np.argmax(predictions.logits, axis=1)[0]
    predicted_label = CLASS_NAMES[predicted_index]

    probabilities = tf.nn.softmax(predictions.logits, axis=-1).numpy()
    confidence = float(probabilities[0][predicted_index])

    return {
        "label": predicted_label,
        "confidence": round(confidence, 4)
    }

@router.post("/predict")
async def predict_face_shape(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File yang diunggah bukan gambar.")

    image_bytes = await file.read()

    try:
        result = predict_image(image_bytes)
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Terjadi kesalahan saat memproses gambar: {str(e)}")