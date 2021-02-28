from kafka.errors import KafkaError

from modules.order.application.event_broker.producer import KafkaProducer
from modules.order.application.unit_of_work import AbstractUnitOfWork
from modules.order.domain.entity import Order as OrderEntity
from modules.order.interface.model import Order as OrderDTO
from modules.order.infrastructure.model import Order as OrderDAO


class OrderService:

    @classmethod
    async def make_order(
            cls,
            order: OrderDTO,
            unit_of_work: AbstractUnitOfWork,
            producer: KafkaProducer
    ):
        entity = OrderEntity(**order.dict())
        with unit_of_work as repo_uow:
            entity.create()
            repo_uow.batches.add(OrderDTO.entity_to_orm(entity))
            repo_uow.commit()

            try:
                await producer.produce_order(order)
            except KafkaError as e:
                repo_uow.rollback(OrderDAO)
                raise e

        return entity
