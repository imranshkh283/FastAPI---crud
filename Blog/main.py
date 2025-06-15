from typing import Annotated
# Annotated is a decorator that adds metadata to the function
from fastapi import FastAPI, Depends, HTTPException, Path, status
# FastAPI is the main class that is used to create the API
# Depends is a decorator that injects the dependency into the function, it is used to inject the database into the function
# HTTPException is a class that is used to raise an exception
# Path is a decorator that validates the path parameter
from . import schemas, models
from .database import engine, get_db
from sqlalchemy.orm import Session
# Session is used to interact with the database
app = FastAPI()

# create_all is used to create the tables in the database
models.Base.metadata.create_all(engine)

@app.get("/")
def root():
    return {"root": "FastApi is working on port 8000"}

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", status_code=status.HTTP_200_OK)
def read_blog(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).offset(skip).limit(limit).all()
    return blogs

@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_blog_by_id(id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog