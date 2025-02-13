"""https://www.codewars.com/kata/6545283611df271da7f8418c/train/python"""

# 3 powers of 2

def three_powers(num):
    if num <= 2:
        return False
    binary = bin(num)[2:]
    if binary.count('1') > 3:
        return False
    return True