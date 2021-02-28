import abc
import logging

from aiokafka import AIOKafkaProducer
from kafka.errors import KafkaError

from modules.order.domain.entity import Order as OrderEntity
from modules.order.interface.model import Order as OrderDTO


log = logging.getLogger(__name__)


class BaseProducer(abc.ABC):

    @abc.abstractmethod
    def produce_order(self, order: OrderEntity):
        raise NotImplementedError


class KafkaProducer(AIOKafkaProducer, BaseProducer):

    async def produce_order(self, order: OrderEntity) -> None:
        try:
            await self.start()
            await self.send("order", OrderDTO.parse_obj(order).json())
        except Exception as e:
            raise KafkaError(e)
        finally:
            await self.stop()
