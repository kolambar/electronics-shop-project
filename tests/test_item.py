"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture()
def test_element():
    return Item("Смартфон", 10000, 20)

def test_calcalculate_total_price(test_element):
    assert test_element.calculate_total_price() == 10000 * 20


def test_apply_discount(test_element):
    test_element.apply_discount()
    assert test_element.price == 10000
    Item.pay_rate = 0.8
    test_element.apply_discount()
    assert test_element.price == 8000.0
