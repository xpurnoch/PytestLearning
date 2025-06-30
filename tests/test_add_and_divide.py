import pytest
import source.add_and_divide as mf

def test_add():
    assert mf.add(1, 2) == 3

def test_divide():
    assert mf.divide(10, 2) == 5

def test_add_strings():
    assert mf.add("A", "B") == "AB"

@pytest.mark.parametrize("one, two", [(1, 2), (3, 4)])
def test_sum(one, two):
    assert one + two == mf.add(one, two)

@pytest.mark.xfail(reason="Division by zero")
def test_divide_by_zero():
    mf.divide(1, 0)
