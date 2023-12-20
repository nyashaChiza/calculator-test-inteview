import pytest
from src import Calculator
import sys

@pytest.fixture
def calculator():
    return Calculator()


##: Implement Your Unit Tests Here
