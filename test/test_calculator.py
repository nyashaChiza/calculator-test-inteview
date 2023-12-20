import pytest
from src import Calculator
import sys

@pytest.fixture
def calculator():
    return Calculator()


##: Implement Your Unit Tests Here

## UNIT TESTING BY BLESSED MUNASHE J CHIHOTA
## DATE: 20/12/2023

# Testing of basic calculator functionality
def test_addition(calculator):
    result = calculator.add(3, 4)
    assert result == 7

def test_subtraction(calculator):
    result = calculator.subtract(7, 4)
    assert result == 3

def test_multiplication(calculator):
    result = calculator.multiply(2, 5)
    assert result == 10

def test_division(calculator):
    result = calculator.divide(10, 2)
    assert result == 5


######################### POTENTIAL ERROR CONDITIONS AND EDGE CASES
def test_division_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)

# Testing basic floating point operation accuracy to at least 10 decimal places
def test_floatingPoint_addition(calculator): 
    result = calculator.add(1.5678868561, 3.586253563)
    assert result == 5.1541404191

def test_floatingPoint_subtraction(calculator):
    result = calculator.subtract(3.586253563, 1.5678868561)
    assert result == 2.0183667069

def test_floatingPoint_multiplication(calculator):
    result = calculator.multiply(1.52567, 2.52673)
    assert result == 3.8549561591000003 ## Remark: Multiplication operation can actually be accurate to 16 decimal places

def test_floatingPoint_division(calculator):
    result = calculator.divide(22, 7)
    assert result == 3.142857142857143
## Remark: Calculated Pie value is accurate to 15 decimal places hence division is accurate to 15 decimal places

################# Testing basic operation on positive and negative integers
def test_addPosNeg(calculator):
    result = calculator.add(-10, 5)
    assert result == -5

def test_subPosNeg(calculator):
    result = calculator.subtract(5, 10)
    assert result == -5

def test_multPosNeg(calculator):
    result = calculator.multiply(5, -10)
    assert result == -50

def test_divPosNeg(calculator):
    result = calculator.divide(5, -10)
    assert result == -0.5

### TESTING EDGE CASES
    
## Operations on the highest positive number
    

def test_add_largest_number(calculator):
    largest_number = sys.float_info.max
    result = calculator.add(largest_number, 2)
    assert result == largest_number + 3  
## Remark: The largest representable floating point number is 1.7976931348623157e+308 (inf). 
    #At this boundary, the add operation fails to differentiate between an addition by 2 and an addition by 3. 

def test_subFrom_largest_number(calculator):
    largest_number = sys.float_info.max
    result = calculator.subtract(largest_number, 2)
    assert result == largest_number - 3  
## Remark: The same remark as in test_add_largest_number holds.
     
def test_multiply_with_largest_number(calculator):
    largest_number = sys.float_info.max
    result = calculator.multiply(largest_number, 2)
    assert result == largest_number * 1.1  
## Remark:  The multiply method passes any result that's about 1.1 times greater than 1.7976931348623157e+308 as it just sees it as infinity (overflow). 
    
def test_divide_largest_number(calculator):
    most_negative_number = sys.float_info.max
    result = calculator.divide(10, most_negative_number)
    assert result == 5.562684646268004e-308
##Remark: The division operation here seems to perform better than the other operations for extreme cases.

## Operations on the lowest positive number
def test_add_smallest_number(calculator):
    smallest_number = sys.float_info.min
    result = calculator.add(smallest_number, 2)
    assert result == 2  
## Remark: The smallest positive representable floating point number is 2.2250738585072014e-308. 
    #At this boundary, the add operation fails to account for the addition of this extremely small value

def test_subtract_smallest_number(calculator):
    smallest_number = sys.float_info.min
    result = calculator.subtract(smallest_number, 2)
    assert result == -2  
## Remark: The smallest positive representable floating point number is 2.2250738585072014e-308. 
    #At this boundary, the subtract operation fails to account for the subtraction of this extremely small value  

def test_multiply_smallest_number(calculator):
    smallest_number = sys.float_info.min
    result = calculator.multiply(smallest_number, smallest_number)
    assert result == 0  
## Remark: The multiplication operation considers the square of the very small numbers to just be zero (underflow)
    
def test_divide_smallest_number(calculator):
    smallest_number = sys.float_info.min
    result = calculator.divide(10, smallest_number)
    assert result == 4.49423283715579e+308  

## Operations on the most negative number
def test_add_most_negative_number(calculator):
    most_negative_number = -sys.float_info.max
    result = calculator.add(most_negative_number, 2)
    assert result == most_negative_number + 3 
##Remark: The addition of 3 or 2 makes no difference to the answer the calculator produces which points to an accuracy limit 

def test_subtract_from_most_negative_number(calculator):
    most_negative_number = -sys.float_info.max
    result = calculator.subtract(most_negative_number, 2)
    assert result == most_negative_number - 3  
##Remark: The subtraction of 3 or 2 makes no difference to the answer the calculator produces which points to an accuracy limit 


def test_multiply_with_most_negative_number(calculator):
    most_negative_number = -sys.float_info.max
    result = calculator.multiply(most_negative_number, 2)
    assert result == most_negative_number * 1.1
##Remark: Multiplication accuracy is compromised past the most negative number limit (overflow)

def test_divide_most_negative_number(calculator):
    most_negative_number = -sys.float_info.max
    result = calculator.divide(10, most_negative_number)
    assert result == -5.562684646268004e-308

## Operations on the least negative number
def test_add_least_negative_number(calculator):
    least_negative_number = -sys.float_info.min
    result = calculator.add(least_negative_number, 2)
    assert result == 2  
##Remark: The least negative number is not registered by the add operation

def test_subtract_least_negative_number(calculator):
    least_negative_number = -sys.float_info.min
    result = calculator.subtract(least_negative_number, 2)
    assert result == -2  
##Remark: The least negative number is not registered by the subtract operation

def test_multiply_with_least_negative_number(calculator):
    least_negative_number = -sys.float_info.min
    result = calculator.multiply(least_negative_number, least_negative_number)
    assert result == 0
##Remark: The test is passed off as 0 which is not accurate. (underflow)

def test_divide_least_negative_number(calculator):
    least_negative_number = -sys.float_info.min
    result = calculator.divide(10, least_negative_number)
    assert result == -4.49423283715579e+308 


## TEST SUMMARY 
    
# The windows 10 Calculator 11.2307.4.0 (© 2023 Microsoft) was used as a benchmark for the test metrics.


# The calculator class performs its four operations accurately for real numbers within the overflow (order of 308) 
# and underflow limits (order of -308). The division operation seems to be the best performing at the edge cases. 
# Furthermore, the calculator displays an accuracy of up to 16 decimal places for
# decimal answers and can represent scientific constants like pie to an accuracy of 15 decimal places.
