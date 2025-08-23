import uvicorn
from app.main import app

app = app

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8015, reload=True)
