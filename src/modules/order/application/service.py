from modules.order.domain.value_object import OrderStatus
from modules.order.application.event_broker.producer import KafkaProducer
from modules.order.application.unit_of_work import AbstractUnitOfWork
from modules.order.domain.entity import Order as OrderEntity


class OrderService:

    @classmethod
    def make_order(
            cls,
            order: OrderEntity,
            unit_of_work: AbstractUnitOfWork,
            producer: KafkaProducer
    ):
        with unit_of_work as repo_uow:
            order.create()
            repo_uow.batches.add(order)
            with producer.transaction() as produce_uow:
                produce_uow.produce_order(order)
                repo_uow.commit()

        return True
