from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"root": "FastApi is working on port 8000"}