import pytest
from to_test import sum_all


@pytest.mark.parametrize('test_args, expected', [
    ((1,), 1),
    ((1, 2, 3), 6),
    ((-10, 5), -5),
    ((1.5, 4.1, 2.0), 7.6),
    ((), 0)
])
def test_sum_all(test_args, expected):
    assert sum_all(*test_args) == expected


def test_sum_all_raises_typeerror_on_inappropriate_args():
    test_arg = '1, 2, 3'

    with pytest.raises(TypeError):
        assert sum_all(test_arg)
