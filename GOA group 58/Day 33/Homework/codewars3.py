"""https://www.codewars.com/kata/57a049e253ba33ac5e000212"""

# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)