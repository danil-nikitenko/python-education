import pytest
from ..practice.linked_list import LinkedList


@pytest.fixture
def linked_list():
    return LinkedList(1, 2, 3)


def test_linked_list_prepend(linked_list):
    linked_list.prepend(0)
    assert linked_list[0] == 0


def test_linked_list_append(linked_list):
    linked_list.append(4)
    assert linked_list[3] == 4


def test_linked_list_lookup(linked_list):
    assert linked_list.lookup(3) == 2


def test_linked_list_insert(linked_list):
    linked_list.insert(2, 4)
    assert linked_list[2] == 4


def test_linked_list_delete(linked_list):
    linked_list.delete(1)
    assert linked_list[1] == 3


def test_linked_list_lookup_raises_value_error(linked_list):
    with pytest.raises(ValueError):
        assert linked_list.lookup(4)


def test_linked_list_delete_raises_index_error(linked_list):
    with pytest.raises(IndexError):
        assert linked_list.delete(3)
