from src.modules.order.application.event_broker import BaseEventBroker
from src.modules.order.application.repository import BaseRepository


class OrderService:
    def make_order(self, repository: BaseRepository, event_broker: BaseEventBroker):
        pass
