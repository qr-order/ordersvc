from typing import List, Optional
from uuid import UUID

import arrow
from pydantic.main import BaseModel

from modules.order.domain.entity import Order as OrderEntity
from modules.order.domain.value_object import OrderStatus


class Order(BaseModel):
    id: Optional[str] = None
    customerPhoneNumber: str
    storeId: str
    itemIds: List[str]
    amount: int
    orderDate: Optional[str] = None
    orderStatus: Optional[int] = None

    def to_entity(self):
        entity = OrderEntity(
            order_id=UUID(self.id) if self.id is not None else None,
            customer_phone_number=self.customerPhoneNumber,
            store_id=UUID(self.storeId),
            item_ids=[UUID(item) for item in self.itemIds],
            amount=self.amount,
            order_date=arrow.get(self.orderDate),
            order_status=OrderStatus(self.orderStatus)
        )
        return entity

    @classmethod
    def serialize(cls, order: OrderEntity):
        return Order(
            order_id=str(order.id),
            customer_phone_number=order.customer_phone_number,
            storeId=str(order.store_id),
            itemIds=[str(item) for item in order.item_ids],
            amount=order.amount,
            orderDate=str(order.order_date),
            orderStatus=int(order.order_status)
        )


