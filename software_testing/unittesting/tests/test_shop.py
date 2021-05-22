import pytest
import sys
sys.path.append('/home/geleoz/snap/python-education/software_testing/unittesting')
from to_test import Product, Shop


@pytest.fixture
def empty_shop():
    return Shop()


@pytest.fixture
def shop():
    return Shop(Product('Apple', 10, 50))


def test_shop_default_initial_products(empty_shop):
    assert empty_shop.products == []


def test_shop_default_initial_money(empty_shop):
    assert empty_shop.money == .0


def test_shop_products_stored_in_list(shop):
    assert isinstance(shop.products, list)


def test_shop_add_product(shop):
    banana = Product('Banana', 15, 35)
    shop.add_product(banana)
    assert banana in shop.products


def test_shop_add_product_raises_typeerror_on_inappropriate_args(shop):
    with pytest.raises(TypeError):
        assert shop.add_product()


def test_shop_get_product_index_product_presented(shop):
    assert shop._get_product_index('Apple') == 0


def test_shop_get_product_index_product_not_presented(shop):
    assert shop._get_product_index('Banana') is None


def test_shop_get_product_raises_typeerror_on_inappropriate_args(shop):
    with pytest.raises(TypeError):
        assert shop._get_product_index()


def test_shop_sell_product_product_index_is_none(shop):
    assert shop.sell_product('Banana') is None


def test_shop_sell_product_raises_valueerror_on_not_enough_products(shop):
    with pytest.raises(ValueError):
        assert shop.sell_product('Apple', 51)


def test_shop_sell_product_del_product(shop):
    shop.sell_product('Apple', 50)
    assert shop._get_product_index('Apple') is None


def test_shop_sell_product_subtract_product(shop):
    shop.sell_product('Apple', 10)
    assert shop.products[shop._get_product_index('Apple')].quantity == 40


def test_shop_sell_product_money_changed(shop):
    shop.sell_product('Apple', 10)
    assert shop.money == 100.0


def test_shop_sell_product_return_receipt(shop):
    assert shop.sell_product('Apple', 10) == 100.0


def test_shop_sell_product_raises_typeerror_on_inappropriate_args(shop):
    with pytest.raises(TypeError):
        assert shop.sell_product()
