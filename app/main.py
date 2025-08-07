from fastapi import FastAPI
from api.v1.endpoints import color_analysis, analysis, bmi, body_shape, face_shape, product, celebrity, product_color_analysis_compatibility, product_bmi_compatibility, product_face_shape_compatibility, product_colors

app = FastAPI()

# app.include_router(face_shape.router)
app.include_router(analysis.router)
app.include_router(bmi.router)
app.include_router(color_analysis.router)
app.include_router(product.router)
app.include_router(body_shape.router)
app.include_router(face_shape.router)
app.include_router(celebrity.router)
app.include_router(product_color_analysis_compatibility.router)
app.include_router(product_bmi_compatibility.router)
app.include_router(product_face_shape_compatibility.router)
app.include_router(product_colors.router)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Tiebymin Analysis API!"}