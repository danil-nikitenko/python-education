import pytest
import sys
sys.path.append('../')
from binary_search import binary_search


@pytest.mark.parametrize('test_args, expected', [
    (((0, 1, 2, 3, 4), 2), 2),
    (((.0, 1.44, 3.8, 12.5), 12.5), 3),
    ((('a', 'b', 'c', 'f', 'k'), 'b'), 1)
])
def test_binary_search(test_args, expected):
    assert binary_search(test_args[0], test_args[1]) == expected
