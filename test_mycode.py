import pytest

from mycode import add_numbers

def test_add_positive():
    assert add_numbers(3, 5) == 8

def test_add_zero():
    assert add_numbers(0, 5) == 5

def test_add_negative():
    assert add_numbers(-3, -5) == -8
