import pytest
import sys
sys.path.append('/home/geleoz/snap/python-education/software_testing/unittesting')
from to_test import Product


@pytest.fixture
def product():
    return Product('Apple', 10, 50)


def test_product_default_initial_quantity():
    product = Product('Banana', 15)
    assert product.quantity == 1


def test_product_raises_typeerror_on_inappropriate_args():
    with pytest.raises(TypeError):
        assert Product('Banana')


def test_product_setting_initial_title(product):
    assert product.title == 'Apple'


def test_product_setting_initial_price(product):
    assert product.price == 10


def test_product_setting_initial_quantity(product):
    assert product.quantity == 50


def test_product_subtract_quantity(product):
    product.subtract_quantity(10)
    assert product.quantity == 40


def test_product_subtract_quantity_none_arg(product):
    product.subtract_quantity()
    assert product.quantity == 49


def test_product_subtract_quantity_raises_typeerror_on_inappropriate_args(product):
    with pytest.raises(TypeError):
        assert product.subtract_quantity('20')


def test_product_add_quantity(product):
    product.add_quantity(10)
    assert product.quantity == 60


def test_product_add_quantity_none_arg(product):
    product.add_quantity()
    assert product.quantity == 51


def test_product_add_quantity_raises_typeerror_on_inappropriate_args(product):
    with pytest.raises(TypeError):
        assert product.add_quantity('20')


def test_product_change_price(product):
    product.change_price(5)
    assert product.price == 5


def test_product_change_price_raises_typeerror_on_none_arg(product):
    with pytest.raises(TypeError):
        assert product.change_price()
