"""https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/python"""

# What is between?

def between(a,b):
    result = []
    for i in range(a, b + 1):
        result.append(i)
    return result