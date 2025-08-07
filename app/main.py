from fastapi import FastAPI
from api.v1.endpoints import face_shape, bmi, analysis

app = FastAPI()

app.include_router(face_shape.router)
app.include_router(analysis.router)
app.include_router(bmi.router)
