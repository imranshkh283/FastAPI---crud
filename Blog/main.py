from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str

@app.get("/")
def root():
    return {"root": "FastApi is working on port 8000"}

@app.post("/blog")
def create_blog(request: Blog):
    return request