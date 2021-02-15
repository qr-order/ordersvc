from fastapi import FastAPI

from api.routes.api import router as api_router


def get_application() -> FastAPI:

    application: FastAPI = FastAPI()

    application.include_router(api_router, prefix="")

    return application


app = get_application()


@app.get("/")
async def root():
    return {"message": "Hello, World"}
