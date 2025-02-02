"""https://www.codewars.com/kata/52f3a8e1f85fadcdf7001e31/train/python/"""

# Factorial division

def factorial_division(n, d):
    product = 1
    for i in range(d + 1, n + 1):
        product *= i
    return product