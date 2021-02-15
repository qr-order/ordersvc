import json
import logging

from fastapi import APIRouter

from core.config import KAFKA_BOOTSTRAP_SERVERS
from database.mysql import SessionLocal
from modules.order.application.event_broker.producer import KafkaProducer
from modules.order.application.service import OrderService
from modules.order.application.unit_of_work import SqlAlchemyUnitOfWork
from modules.order.interface.model import Order

router = APIRouter()

log = logging.getLogger(__name__)


@router.post("/")
async def make_order(order: Order):
    producer = KafkaProducer(
        value_serializer=serializer,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        enable_idempotence=True,
        acks=2
    )
    unit_of_work = SqlAlchemyUnitOfWork(SessionLocal)

    order = await OrderService.make_order(order=order.to_entity(), producer=producer, unit_of_work=unit_of_work)

    return order


def serializer(value):
    return json.dumps(value).encode()
