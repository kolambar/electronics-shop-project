from src.phone import Phone
import pytest


@pytest.fixture()
def test_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test___str__(test_phone):
    assert str(test_phone) == 'iPhone 14'


def test___repr__(test_phone):
    assert repr(test_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_num_of_sim(test_phone):
    test_phone.number_of_sim = 1
    assert test_phone.number_of_sim == 1


def test_num_of_sim_err(test_phone):
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 0


def test___add__(test_phone):
    phone_2 = Phone("iPhone 13", 80_000, 10, 2)
    assert test_phone + phone_2 == 15
