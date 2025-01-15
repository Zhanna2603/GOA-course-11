"""https://www.codewars.com/kata/52f3149496de55aded000410/train/python"""

# Summing a number's digits

def sum_digits(number):
    num_str = str(abs(number))
    sum = 0
    for digit in num_str:
        sum += int(digit)
    return sum