from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def make_order():
    pass
