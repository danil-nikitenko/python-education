import pytest
import sys
sys.path.append('../')
from practice.binary_search_tree import BinarySearchTree


@pytest.fixture
def binary_search_tree():
    return BinarySearchTree(50, 40, 30, 35, 55)


def test_binary_search_tree_lookup(binary_search_tree):
    assert binary_search_tree.lookup(35).data == 35


def test_binary_search_tree_insert(binary_search_tree):
    binary_search_tree.insert(15)
    assert binary_search_tree.lookup(15)


def test_binary_search_tree_delete(binary_search_tree):
    binary_search_tree.delete(50)
    with pytest.raises(ValueError):
        assert binary_search_tree.lookup(50)
