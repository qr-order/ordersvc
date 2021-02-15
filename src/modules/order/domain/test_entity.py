from collections import namedtuple
from uuid import uuid4

import arrow
import pytest

from modules.order.domain.entity import Order

import logging

log = logging.getLogger(__name__)


def get_entity_test_case():
    test = namedtuple(
        'test',
        ('case_name', 'order', 'expected_error', 'expected_error_str')
    )
    test_cases = [
        test(
            case_name='basic case',
            order=dict(
                customer_phone_number='01091207304',
                store_id=uuid4(),
                item_ids=[uuid4() for _ in range(5)],
                amount=40000,
            ),
            expected_error=None,
            expected_error_str=''
        ),
        test(
            case_name='',
            order=dict(
                order_id=uuid4(),
                customer_phone_number='01091207304',
                store_id=uuid4(),
                item_ids=[uuid4() for _ in range(5)],
                amount=40000,
                order_date=arrow.utcnow().datetime,
                order_status=1
            ),
            expected_error=None,
            expected_error_str=''
        ),
        test(
            case_name='',
            order=dict(
                order_id=uuid4(),
                customer_phone_number='01091207304',
                store_id=uuid4(),
                item_ids=[uuid4() for _ in range(5)],
                amount=40000,
                order_date=arrow.utcnow().datetime,
                order_status=6
            ),
            expected_error=ValueError,
            expected_error_str='not a valid OrderStatus'
        ),
    ]
    return test_cases


@pytest.mark.parametrize('case_name, order, expected_error, expected_error_str', get_entity_test_case())
def test_init_order_entity(case_name, order, expected_error, expected_error_str):
    if expected_error is not None:
        with pytest.raises(expected_error) as error:
            Order(**order)
        assert expected_error_str in str(error.value)
    else:
        entity = Order(**order)
        assert isinstance(entity, Order)
