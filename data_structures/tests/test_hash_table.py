import pytest
from ..practice.hash_table import HashTable


@pytest.fixture
def hash_table():
    hash_table = HashTable(15)
    hash_table.insert(1, 1)
    hash_table.insert(2, 2)
    hash_table.insert(3, 3)
    return hash_table


def test_hash_table_lookup(hash_table):
    assert hash_table.lookup(2) == 2


def test_hash_table_insert(hash_table):
    hash_table.insert(4, 4)
    assert hash_table.lookup(4) == 4


def test_hash_table_delete(hash_table):
    hash_table.delete(3)
    with pytest.raises(KeyError):
        assert hash_table.lookup(3)


def test_hash_table_delete_raises_key_error(hash_table):
    with pytest.raises(KeyError):
        assert hash_table.delete(5)


def test_hash_table_hash_function_raises_type_error(hash_table):
    with pytest.raises(TypeError):
        assert hash_table.hash_function(5.55)


def test_hash_table_collision_handling(hash_table):
    hash_table.insert('lies', 'lies')
    hash_table.insert('foes', 'foes')
    assert hash_table.lookup('lies') != hash_table.lookup('foes')
