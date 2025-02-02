"""https://www.codewars.com/kata/57d0089e05c186ccb600035e/train/python"""

# Check if a triangle is an equable triangle!

def equable_triangle(a,b,c):
    p = a + b + c
    h_p = p / 2
    return p == (h_p * (h_p - a) * (h_p - b) * (h_p - c)) ** 0.5