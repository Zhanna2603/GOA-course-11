"""https://www.codewars.com/kata/514b92a657cdc65150000006"""

# Multiples of 3 or 5

def solution(number):
    if number < 0:
        return 0
    
    mult_sum = 0
    for i in range (number):
        if i % 5 == 0 or i % 3 == 0:
            mult_sum += i
    return mult_sum