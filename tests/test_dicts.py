import pytest


from utils.dicts import get_val


data = {'name': 'Vladimir', 'surname': 'Semikov', 'age': 27}


def test_get_val():
    assert get_val(data, 'surname') == 'Semikov'
    assert get_val(data, 'name') == 'Vladimir'
    assert get_val(data, 'age') == 27
    assert get_val(data, 'education') == 'git'
    assert get_val(data, 'education', 'not found') == 'not found'
