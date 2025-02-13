"""Write a function that takes a list of numbers as input and returns the sum of all the numbers that are greater than 10"""

def greater_than_10(num):
    return sum(n for n in num if num > 10)