from fastapi import FastAPI
import uvicorn

app = FastAPI()

port = 9000
@app.get("/")
def root():
    return {"root": "FastApi is working on port 9000"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=port)