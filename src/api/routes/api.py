from fastapi import APIRouter

from src.modules.order.interface import controller

router = APIRouter()
router.include_router(controller.router, tags=["orders"], prefix="/orders")
