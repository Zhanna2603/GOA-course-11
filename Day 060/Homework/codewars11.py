"""https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python"""

# CamelCase Method

def camel_case(s):
    words = s.split()
    return ''.join(word.capitalize() for word in words)