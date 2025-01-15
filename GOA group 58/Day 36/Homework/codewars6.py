"""https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python"""

# Bit Counting

def count_bits(n):
    result = ""
    while n != 0:
        result += str(n % 2)
        n //= 2
    return result[::-1].count("1")
