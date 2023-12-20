import pytest
from src import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add_positive_numbers(calculator):
    assert calculator.add(2, 3) == 5.0
##: Implement Your Unit Tests Here
