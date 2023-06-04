import pytest

from utils import arrs


@pytest.fixture()
def array_fixture():
    return [1, 2, 3, 4, 5]


def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get(array_fixture, -1, "test") == "test"


def test_get_index_out_of_range(array_fixture):
    with pytest.raises(IndexError):
        arrs.get([], 0)
        arrs.get(array_fixture, 8)


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4, 5]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(array_fixture, -1) == [5]
    assert arrs.my_slice(array_fixture, -2) == [4, 5]
    assert arrs.my_slice(array_fixture, -6, 3) == [1, 2, 3]
