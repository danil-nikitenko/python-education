import pytest
from ..iterative_quick_sort import iterative_quick_sort


def test_iterative_quick_sort_int():
    lst1 = lst2 = [4, 2, 4, 11, 50, 32, 3, 0]
    iterative_quick_sort(lst1)
    lst2.sort()
    assert lst1 == lst2


def test_iterative_quick_sort_float():
    lst1 = lst2 = [4.3, 2.1, 4.0, 11.51, 50.9, 32.111, 3.3, .0]
    iterative_quick_sort(lst1)
    lst2.sort()
    assert lst1 == lst2


def test_iterative_quick_sort_chars():
    lst1 = lst2 = ['d', 'a', 'm', 's', 'f', 'a', 'y']
    iterative_quick_sort(lst1)
    lst2.sort()
    assert lst1 == lst2
