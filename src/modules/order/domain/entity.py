from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from uuid import uuid4, UUID

import arrow

from modules.order.domain.value_object import OrderStatus


@dataclass
class Order:
    __id: Optional[UUID]
    __customer_phone_number: str
    __store_id: UUID
    __item_ids: List[UUID]
    __amount: int
    __order_date: Optional[datetime]
    __order_status: Optional[OrderStatus]

    def __init__(self,
                 customer_phone_number: str,
                 store_id: UUID,
                 item_ids: List[UUID],
                 amount: int,
                 order_id: UUID = None,
                 order_date: datetime = None,
                 order_status: int = None,
                 ):
        self.__id = order_id
        self.__customer_phone_number = customer_phone_number
        self.__store_id = store_id
        self.__item_ids = item_ids
        self.__amount = amount

        self.__order_date = order_date
        self.__order_status = OrderStatus(order_status) if order_status is not None else None

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return other.__id == self.__id

    def __hash__(self):
        return hash(self.__id)

    @property
    def id(self):
        return self.__id

    @property
    def customer_phone_number(self):
        return self.__customer_phone_number

    @property
    def store_id(self):
        return self.__store_id

    @property
    def item_ids(self):
        return self.__item_ids

    @property
    def amount(self):
        return self.__amount

    @property
    def order_date(self):
        return self.__order_date

    @property
    def order_status(self):
        return self.__order_status

    def create(self):
        self.__validate_creation()

        self.__id = uuid4()
        self.__order_date = arrow.utcnow().datetime
        self.__order_status = OrderStatus.PUBLISHED
        return self.__id

    def cancel_order_by_store(self) -> OrderStatus:
        self.__validate_cancel_order()
        return self.change_status(status=OrderStatus.CANCELED_BY_STORE)

    def cancel_order_by_customer(self) -> OrderStatus:
        self.__validate_cancel_order()
        return self.change_status(status=OrderStatus.CANCELED_BY_CUSTOMER)

    def change_status(self, status: int) -> OrderStatus:
        self.__order_status = OrderStatus(status)
        return self.__order_status

    def __validate_creation(self):
        if self.__id is not None:
            raise OrderCreationError(f'The order has already been created. id: {self.__id}')

    def __validate_cancel_order(self) -> None:
        if self.__order_status in (OrderStatus.APPROVED, OrderStatus.COMPLETED):
            raise CancelOrderValidationError(f'The order has already been {self.__order_status.name.lower()}')


class OrderCreationError(Exception):
    pass


class CancelOrderValidationError(Exception):
    pass
