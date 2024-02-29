'''My calculator test'''
import pytest
from calculator import add, subtract, multiply, divide

# pylint: disable=invalid-name

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (0, 0, 0),
    (-1, -1, -2),
    (100, 100, 200)
])
def test_addition(a, b, expected):
    '''Test addition with multiple inputs to ensure correctness'''
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 0),
    (0, 0, 0),
    (-1, -1, 0),
    (100, 50, 50)
])
def test_subtraction(a, b, expected):
    '''Test subtraction with various inputs'''
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (0, 0, 0),
    (-1, -1, 1),
    (10, 5, 50)
])
def test_multiply(a, b, expected):
    '''Test multiplication for correct results across different scenarios'''
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 1),
    (0, 1, 0),
    (-1, -1, 1),
    (10, 5, 2)
])
def test_divide(a, b, expected):
    '''Test division, including edge cases'''
    assert divide(a, b) == expected

def test_divide_by_zero():
    '''Ensure division by zero is handled, if applicable'''
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
