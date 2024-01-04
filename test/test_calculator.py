import pytest
from .. import Calculator

# Creating an instance of the Calculator class for testing....
calculator = Calculator()

# Test cases for the Calculator class
def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0
    assert calculator.add(0, -5) == -5
    assert calculator.add(3.5, 2.5) == 6.0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(1, 1) == 0
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-5, 2) == -7
    assert calculator.subtract(3.5, 2.5) == 1.0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(3, 0) == 0
    assert calculator.multiply(3.5, 2) == 7.0

def test_divide():
    assert calculator.divide(6, 2) == 3.0
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(7, 3) == pytest.approx(2.33333, abs=0.00001)  # Floating-point precision
    with pytest.raises(ValueError):
        calculator.divide(1, 0)  # Division by zero should raise an error
    with pytest.raises(ValueError):
        calculator.divide(0, 0)  # Division by zero should raise an error
    with pytest.raises(ValueError):
        calculator.divide(10, 0.0)  # Division by zero should raise an error

# Additional tests for edge cases and potential error conditions
def test_divide_by_zero_error():
    with pytest.raises(ValueError):
        calculator.divide(1, 0)  # Division by zero should raise an error

def test_invalid_input_types():
    with pytest.raises(TypeError):
        calculator.add("5", 2)  # Invalid input types should raise a TypeError
    with pytest.raises(TypeError):
        calculator.subtract(3, "2")  # Invalid input types should raise a TypeError
    with pytest.raises(TypeError):
        calculator.multiply("3", 2)  # Invalid input types should raise a TypeError
    with pytest.raises(TypeError):
        calculator.divide(6, "2")  # Invalid input types should raise a TypeError

def test_large_numbers():
    # Test multiplication with large numbers
    assert calculator.multiply(10**10, 10**10) == 10**20
    # Test addition with large numbers
    assert calculator.add(10**20, -10**20) == 0

def test_decimal_precision():
    # Test division with decimal precision
    assert calculator.divide(1, 3) == pytest.approx(0.33333, abs=0.00001)
    assert calculator.divide(2, 3) == pytest.approx(0.66666, abs=0.00001)
