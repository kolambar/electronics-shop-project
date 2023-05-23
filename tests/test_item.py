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


def test_instantiate_from_csv():
    list_of_instance = Item.instantiate_from_csv()
    assert type(list_of_instance) == list
    assert list_of_instance[0].name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('15') == 15
    assert Item.string_to_number('15.6') == 16
    assert Item.string_to_number('15.4') == 15

def test_string_to_num_without_dig():
        with pytest.raises(TypeError):
            Item.string_to_number('asd')


def test___str__(test_element):
    assert str(test_element) == 'Смартфон'


def test___repr__(test_element):
    assert repr(test_element) == "Item('Смартфон', 10000, 20)"
