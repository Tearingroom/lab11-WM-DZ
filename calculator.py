"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)
    except TypeError:
        raise TypeError("Input must be a number.")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("Inputs must be numbers.")

def add(a, b):
    return (a+b)

def sub(a,b):
    return (a-b)

def mul(a,b):
    return a*b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def log(a, b):
    if b <= 0 or a <= 0 or a == 1:
        raise ValueError("Invalid log arguments")
    return math.log(b, a)

def exp(a,b):
    return (a**b)