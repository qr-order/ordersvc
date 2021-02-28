from datetime import datetime
from typing import List, Optional
from uuid import UUID

import phonenumbers
from humps import camel
from pydantic import validator, ValidationError

from pydantic.main import BaseModel
from modules.order.domain.entity import Order as OrderEntity
from modules.order.infrastructure.model import Order as OrderDAO


def to_camel(string):
    return camel.case(string)


class Order(BaseModel):
    id: Optional[UUID] = None
    customer_phone_number: str
    store_id: UUID
    item_ids: List[UUID]
    amount: int
    order_date: Optional[datetime] = None
    order_status: Optional[int] = None

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
        orm_mode = True

    @classmethod
    def entity_to_orm(cls, order: OrderEntity):
        return OrderDAO(
            id=str(order.id),
            customer_phone_number=order.customer_phone_number,
            store_id=str(order.store_id),
            item_ids=[str(item) for item in order.item_ids],
            amount=order.amount,
            order_date=str(order.order_date),
            order_status=int(order.order_status)
        )

    @validator('customer_phone_number')
    def validate_kr_phone_number(cls, pn):
        try:
            parsed_pn = phonenumbers.parse(pn, 'KR')
            if not phonenumbers.is_valid_number(parsed_pn):
                raise ValueError('invalid phone number')
        except Exception as e:
            raise ValidationError(e)

        return pn

    @validator('amount')
    def amount_must_be_positive_number(cls, num):
        if num < 0:
            raise ValidationError('amount must be positive number')
        return num
