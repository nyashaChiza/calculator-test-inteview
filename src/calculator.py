class Calculator:
   
    """
    A simple calculator class that provides basic arithmetic operations.

    Methods:
    --------
    add(x: float, y: float) -> float:
        Returns the sum of two numbers x and y.

    subtract(x: float, y: float) -> float:
        Returns the difference between two numbers x and y.

    multiply(x: float, y: float) -> float:
        Returns the product of two numbers x and y.

    divide(x: float, y: float) -> float:
        Returns the quotient of two numbers x and y.
        Raises a ValueError if y is zero.

    Example:
    --------
    >>> calc = Calculator()
    >>> calc.add(2, 3)
    5.0
    >>> calc.subtract(5, 2)
    3.0
    >>> calc.multiply(2, 4)
    8.0
    >>> calc.divide(10, 5)
    2.0
    >>> calc.divide(10, 0)
    ValueError: Cannot divide by zero
    """
    
    
    def add(self, x:float, y:float)->float:
        return float(x + y)

    def subtract(self, x:float, y:float)->float:
        return float(x - y)

    def multiply(self, x:float, y:float)->float:
        return float(x * y)

    def divide(self, x:float, y:float)->float:
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return float(x / y)
