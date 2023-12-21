import pytest
from src import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add_positive_numbers(calculator):
    assert calculator.add(2, 3) == 5.0
# Above is an example unit test, implement your own unit tests below
## Unit tests for negative and positive numbers
def test_add_negative_numbers(calculator):
    result = calculator.add(-2, -3)
    assert result == -5.0

def test_add_zero(calculator):
    result = calculator.add(0, 0)
    assert result == 0.0

def test_subtract_positive_numbers(calculator):
    result = calculator.subtract(5, 2)
    assert result == 3.0

def test_subtract_negative_numbers(calculator):
    result = calculator.subtract(-5, -2)
    assert result == -3.0

def test_subtract_zero(calculator):
    result = calculator.subtract(5, 5)
    assert result == 0.0

def test_multiply_positive_numbers(calculator):
    result = calculator.multiply(2, 4)
    assert result == 8.0

def test_multiply_negative_numbers(calculator):
    result = calculator.multiply(-2, 4)
    assert result == -8.0

def test_multiply_zero(calculator):
    result = calculator.multiply(5, 0)
    assert result == 0.0

def test_divide_positive_numbers(calculator):
    result = calculator.divide(10, 5)
    assert result == 2.0

def test_divide_negative_numbers(calculator):
    result = calculator.divide(-10, 5)
    assert result == -2.0

##Edge Case Division by zero
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
       
##Edge case Large numbers

def test_multiply_large_numbers(calculator):
    result = calculator.multiply(10**20, 2)
    assert result == 2 * 10**20

#Edge Case combination of operations 
def test_combined_operations(calculator):
    result = calculator.add(10, calculator.multiply(5, calculator.divide(20, 4)))
    assert result == 35

##Edge case non numeric inputs
def test_non_numeric_input(calculator):
    with pytest.raises(TypeError, match="unsupported operand type(s) for +"):
        calculator.add("5", 5)

##Floating point precision
def test_divide_floats(calculator):
    result = calculator.divide(1.0, 3)
    assert result == pytest.approx(0.3333, rel=1e-3)

##Result exceeding floating limit
def test_overflow_error(calculator):
    with pytest.raises(OverflowError, match="Result exceeds floating-point limits"):
        calculator.add(float('inf'), 1)

