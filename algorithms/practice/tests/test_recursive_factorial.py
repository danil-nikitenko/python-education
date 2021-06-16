import pytest
from ..recursive_factorial import factorial


@pytest.mark.parametrize('test_arg, expected', [
    (5, 120),
    (8, 40320),
    (0, 1)
])
def test_recursive_factorial(test_arg, expected):
    assert factorial(test_arg) == expected


def test_recursive_factorial__raises_typeerror():
    with pytest.raises(TypeError):
        assert factorial('10')


def test_recursive_factorial__raises_recursionerror():
    with pytest.raises(RecursionError):
        assert factorial(-1)
