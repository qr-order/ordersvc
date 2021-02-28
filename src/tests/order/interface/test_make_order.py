import uuid
from collections import namedtuple

import pytest
from faker import Faker
from sqlalchemy.orm import Session

from modules.order.infrastructure.model import Order


fake = Faker()

VALID_STORE_ID = str(uuid.uuid4())

VALID_ITEM_IDS = [str(uuid.uuid4()) for _ in range(3)]

VALID_PHONE_NUMBER = '01012345678'
INVALID_PHONE_NUMBER = '001234'

VALID_AMOUNT = 10000
INVALID_AMOUNT = -1


def get_test_case():

    test = namedtuple('test', ('case_name', 'order', 'expected_status_code'))

    test_sequence = [
        test(
            case_name='basic case',
            order={
                "customerPhoneNumber": VALID_PHONE_NUMBER,
                "storeId": VALID_STORE_ID,
                "itemIds": VALID_ITEM_IDS,
                "amount": VALID_AMOUNT
            },

            expected_status_code=201
        ),
        test(
            case_name='wrong phone number',
            order={
                "customerPhoneNumber": INVALID_PHONE_NUMBER,
                "storeId": VALID_STORE_ID,
                "itemIds": VALID_ITEM_IDS,
                "amount": VALID_AMOUNT
            },
            expected_status_code=422
        ),
        test(
            case_name='invalid amount',
            order={
                "customerPhoneNumber": VALID_PHONE_NUMBER,
                "storeId": VALID_STORE_ID,
                "itemIds": VALID_ITEM_IDS,
                "amount": INVALID_AMOUNT
            },
            expected_status_code=422
        ),
    ]

    return test_sequence


@pytest.mark.parametrize('case_name, order, expected_status_code', get_test_case())
def test_make_order(case_name, order, expected_status_code, client, db: Session):
    response = client.post('/orders', json=order)

    assert expected_status_code == response.status_code

    if expected_status_code == 201:
        order_id = response.json()['id']
        assert db.query(Order).filter_by(id=order_id).one().id == order_id
