from enum import IntEnum


class OrderStatus(IntEnum):
    PUBLISHED = 0
    APPROVED = 1
    CANCELED_BY_STORE = 2
    COMPLETED = 3
    CANCELED_BY_CUSTOMER = 4
    CREATED = 5
