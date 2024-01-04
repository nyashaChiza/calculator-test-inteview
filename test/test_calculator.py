import pytest
from src import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add_positive_numbers(calculator):
    assert calculator.add(2, 3) == 5.0
# Above is an example unit test, implement your own unit tests below


def test_add_all_numbers():
    calc = Calculator()
    assert calc.add(2, 3) == 5.0
    assert calc.add(-5, 7.5) == 2.5
    assert calc.add(0, 0) == 0.0


def test_add_negative_numbers(calculator):
    assert calculator.add(-5, -2) == -7.0



def test_subtract_numbers():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3.0
    assert calc.subtract(10, 3.5) == 6.5
    assert calc.subtract(0, 0) == 0.0

def test_subtract_negative_numbers(calculator):
    assert calculator.subtract(-5, -2) == -3.0    
    
def test_subtract_negative_number(calculator):
    assert calculator.subtract(5, -2) == 7.0        
    
def test_multiply_numbers():
    calc = Calculator()
    assert calc.multiply(2, 4) == 8.0
    assert calc.multiply(-3, 5) == -15.0
    assert calc.multiply(0, 100) == 0.0


def test_multiply_negative_numbers(calculator):
    assert calculator.multiply(-3, -5) == 15.0

def test_divide_small_numbers(calculator):
    result = calculator.divide(1e-20, 1e-20)
    assert result == 1.0

def test_divide_large_numbers(calculator):
    result = calculator.divide(1e20, 1e20)
    assert result == 1.0


def test_divide_negative_numbers(calculator):
    assert calculator.divide(-10, -2) == 5.0



def test_divide_negative_number(calculator):
    assert calculator.divide(10, -5) == -2.0

def test_divide_positive_number():
    calc = Calculator()
    assert calc.divide(10, 5) == 2.0
    assert calc.divide(8, 2) == 4.0




def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)    