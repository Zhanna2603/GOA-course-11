"""https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd"""

# Greatest common divisor

def mygcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x