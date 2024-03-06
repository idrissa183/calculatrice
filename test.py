import pytest
from app import add


def test_add_with_two_positives_numbers():
    assert add(10, 20) == 30


def test_add_with_two_negatives_numbers():
    assert add(-5, -100) == -105


def test_add_with_two_zeros():
    assert add(0, 0) == 0


def test_add_with_two_booleans():
    assert add(True, False) == 1
    assert add(True, True) == 2
    assert add(False, True) == 1
    assert add(False, False) == 0


def test_add_with_two_strings():
    assert add("a", "b") == "ab"


def test_add_with_two_None():
    with pytest.raises(TypeError):
        add(None, None)
