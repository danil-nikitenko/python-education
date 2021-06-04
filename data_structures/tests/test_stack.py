import pytest
from ..practice.stack import Stack


@pytest.fixture
def stack():
    return Stack(1, 2)


def test_stack_peek(stack):
    assert stack.peek() == 2


def test_stack_push(stack):
    stack.push(3)
    assert stack.peek() == 3


def test_stack_pop(stack):
    assert stack.pop() == 2


def test_stack_peek_raises_value_error(stack):
    stack.pop()
    stack.pop()
    with pytest.raises(ValueError):
        assert stack.peek()


def test_stack_pop_raises_value_error(stack):
    stack.pop()
    stack.pop()
    with pytest.raises(ValueError):
        assert stack.pop()
