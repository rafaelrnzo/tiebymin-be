from fastapi import FastAPI
from api.v1.endpoints import face_shape, bmi

app = FastAPI()

app.include_router(face_shape.router)
app.include_router(bmi.router)
