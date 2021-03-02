import json

from fastapi import APIRouter

from core.config import KAFKA_BOOTSTRAP_SERVERS
from database.postgresql import SessionLocal
from modules.order.application.event_broker.producer import KafkaProducer
from modules.order.application.service import OrderService
from modules.order.application.unit_of_work import SqlAlchemyUnitOfWork
from modules.order.interface.model import Order

router = APIRouter()


@router.post('', response_model=Order, status_code=201)
async def make_order(order: Order):
    producer = KafkaProducer(
        value_serializer=serializer,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    )
    unit_of_work = SqlAlchemyUnitOfWork(SessionLocal)

    result = await OrderService.make_order(order=order, producer=producer, unit_of_work=unit_of_work)

    return result


def serializer(value):
    return json.dumps(value).encode()
