from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routes.api import router as api_router


def get_application() -> FastAPI:

    application: FastAPI = FastAPI()

    application.include_router(api_router, prefix="")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_application()


@app.get("/")
async def root():
    return {"message": "Hello, World"}
