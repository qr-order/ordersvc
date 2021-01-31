import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    print("Hello World!")
    return {"message": "Hello, World"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
