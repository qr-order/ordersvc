from typing import List

from pydantic.main import BaseModel


class Order(BaseModel):
    id: int
    customerPhoneNumber: str
    storeId: int
    itemIds: List[int]
    amount: int
    orderDate: str
