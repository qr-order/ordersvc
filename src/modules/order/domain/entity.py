from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from uuid import uuid4, UUID

import arrow

from modules.order.domain.value_object import OrderStatus


@dataclass
class Order:
    id: Optional[UUID]
    customer_phone_number: str
    store_id: UUID
    item_ids: List[UUID]
    amount: int
    order_date: Optional[datetime]
    order_status: Optional[OrderStatus]

    def __init__(self,
                 customer_phone_number: str,
                 store_id: UUID,
                 item_ids: List[UUID],
                 amount: int,
                 id: UUID = None,
                 order_date: datetime = None,
                 order_status: int = None,
                 ):
        self.id = id
        self.customer_phone_number = customer_phone_number
        self.store_id = store_id
        self.item_ids = item_ids
        self.amount = amount

        self.order_date = order_date
        self.order_status = OrderStatus(order_status) if order_status is not None else None

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)

    def create(self):
        self._validate_creation()

        self.id = uuid4()
        self.order_date = arrow.utcnow().datetime
        self.order_status = OrderStatus.PUBLISHED
        return self.id

    def cancel_order_by_store(self) -> OrderStatus:
        self._validate_cancel_order()
        return self.change_status(status=OrderStatus.CANCELED_BY_STORE)

    def cancel_order_by_customer(self) -> OrderStatus:
        self._validate_cancel_order()
        return self.change_status(status=OrderStatus.CANCELED_BY_CUSTOMER)

    def change_status(self, status: int) -> OrderStatus:
        self.order_status = OrderStatus(status)
        return self.order_status

    def _validate_creation(self):
        if self.id is not None:
            raise OrderCreationError(f'The order has already been created. id: {self.id}')

    def _validate_cancel_order(self) -> None:
        if self.order_status in (OrderStatus.APPROVED, OrderStatus.COMPLETED):
            raise CancelOrderValidationError(f'The order has already been {self.order_status.name.lower()}')


class OrderCreationError(Exception):
    pass


class CancelOrderValidationError(Exception):
    pass
