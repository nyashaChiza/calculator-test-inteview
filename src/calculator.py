class Calculator:
    def add(self, x:int, y:int)->int:
        return x + y

    def subtract(self, x:int, y:int)->int:
        return x - y

    def multiply(self, x:int, y:int)->int:
        return x * y

    def divide(self, x:int, y:int)->int:
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return int(x / y)
