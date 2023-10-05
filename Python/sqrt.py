"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
"""

def my_sqrt(x:int)->int:
    x = x ** 0.5
    return int(x)

x = 16
print(my_sqrt(x))