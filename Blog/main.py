from fastapi import FastAPI
from . import schemas, models
from .database import engine
app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/")
def root():
    return {"root": "FastApi is working on port 8000"}

@app.post("/blog")
def create_blog(request: schemas.Blog):
    return request