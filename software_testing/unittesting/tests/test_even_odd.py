import pytest
from to_test import even_odd


@pytest.mark.parametrize('test_arg, expected', [
    (1, 'odd'),
    (6, 'even'),
    (-2, 'even'),
    (0, 'even'),
    (1.5, 'odd'),
    (4.0, 'even')
])
def test_even_odd(test_arg, expected):
    assert even_odd(test_arg) == expected


def test_even_odd_raises_typeerror_on_inappropriate_args():
    test_arg = 'str'

    with pytest.raises(TypeError):
        assert even_odd(test_arg)
