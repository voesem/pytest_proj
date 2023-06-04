import pytest


from utils.dicts import get_val


@pytest.fixture()
def data_fixture():
    return {'name': 'Vladimir', 'surname': 'Semikov', 'age': 27}


def test_get_val(data_fixture):
    assert get_val(data_fixture, 'surname') == 'Semikov'
    assert get_val(data_fixture, 'name') == 'Vladimir'
    assert get_val(data_fixture, 'age') == 27
    assert get_val(data_fixture, 'education') == 'git'
    assert get_val(data_fixture, 'education', 'not found') == 'not found'
    assert get_val('abcdefg', 'name') == 'git'
