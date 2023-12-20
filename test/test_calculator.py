import pytest
from src import Calculator

@pytest.fixture
def calculator():
    return Calculator()


##: Implement Your Unit Tests Here
