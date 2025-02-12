"""https://www.codewars.com/kata/59811fd8a070625d4c000013/train/python"""

# Find the Integral

def integrate(coefficient, exponent):
    new_exponent = exponent + 1
    new_coefficient = coefficient // new_exponent
    return f"{new_coefficient}x^{new_exponent}"