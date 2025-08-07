from fastapi import FastAPI
from api.v1.endpoints import analysis, bmi, body_shape, face_shape

app = FastAPI()

# app.include_router(face_shape.router)
app.include_router(analysis.router)
app.include_router(bmi.router)
app.include_router(body_shape.router)
app.include_router(face_shape.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Tiebymin Analysis API!"}