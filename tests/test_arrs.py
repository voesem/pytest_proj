import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -1, "test") == "test"


def test_get_index_out_of_range():
    with pytest.raises(IndexError):
        arrs.get([], 0)
        arrs.get([1, 2, 3], 6)


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4], -1) == [4]
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -6, 3) == [1, 2, 3]
