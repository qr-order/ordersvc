from sqlalchemy import Column, String, ARRAY, DateTime, Enum
from sqlalchemy.dialects.mysql import INTEGER

from database.postgresql import Base
from modules.order.domain.value_object import OrderStatus


class Order(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, index=True)
    customer_phone_number = Column(String, index=True)
    store_id = Column(String, index=True)
    item_ids = Column(ARRAY(String))
    amount = Column(INTEGER(unsigned=True))
    order_date = Column(DateTime)
    order_status = Column(Enum(OrderStatus))
