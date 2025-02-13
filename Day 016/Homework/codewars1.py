"""https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python"""

# Sum of Multiples

def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    k = (m - 1) // n
    return n * k * (k + 1) // 2