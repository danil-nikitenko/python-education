import pytest
from ..practice.linked_list import LinkedList
from ..practice.graph import Graph


@pytest.fixture
def graph():
    edg = LinkedList(LinkedList(0, 1), LinkedList(0, 2), LinkedList(1, 4))
    return Graph(edg)


def test_graph_lookup(graph):
    assert graph.lookup(2).data == 2


def test_graph_insert(graph):
    graph.insert(5, LinkedList(1, 2))
    assert graph.lookup(5)


def test_graph_delete(graph):
    graph.delete(2)
    with pytest.raises(ValueError):
        assert graph.lookup(2)


def test_graph_delete_raises_value_error(graph):
    with pytest.raises(ValueError):
        assert graph.delete(5)
