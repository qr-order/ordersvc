import abc
import logging

from aiokafka import AIOKafkaProducer

from modules.order.domain.entity import Order as OrderEntity
from modules.order.interface.model import Order as OrderDTO


log = logging.getLogger(__name__)


class BaseProducer(abc.ABC):

    @abc.abstractmethod
    def produce_order(self, order: OrderEntity):
        raise NotImplementedError


class KafkaProducer(BaseProducer, AIOKafkaProducer):

    def produce_order(self, order: OrderEntity) -> None:
        self.send_and_wait("order", OrderDTO.serialize(order))
