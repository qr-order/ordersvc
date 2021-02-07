from modules.order.application.event_broker import BaseEventBroker
from modules.order.application.repository import BaseRepository


class OrderService:
    def make_order(
            self,
            repository: BaseRepository,
            event_broker: BaseEventBroker
    ):
        pass
