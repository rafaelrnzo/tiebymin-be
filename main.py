"""
Entrypoint script to run FastAPI app from project root.
Usage: python main.py
"""
import uvicorn
from app.main import app  # Expose the app variable for uvicorn

# Expose the app variable for uvicorn
app = app

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8015, reload=True)
