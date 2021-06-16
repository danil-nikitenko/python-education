import pytest
from ..practice.queue import Queue


@pytest.fixture
def queue():
    return Queue(1)


def test_queue_peek(queue):
    assert queue.peek() == 1


def test_queue_enqueue(queue):
    queue.enqueue(2)
    queue.dequeue()
    assert queue.peek() == 2


def test_queue_dequeue(queue):
    assert queue.dequeue() == 1


def test_queue_peek_raises_value_error(queue):
    queue.dequeue()
    with pytest.raises(ValueError):
        assert queue.peek()


def test_queue_dequeue_raises_value_error(queue):
    queue.dequeue()
    with pytest.raises(ValueError):
        assert queue.dequeue()
