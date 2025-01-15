"""https://www.codewars.com/kata/58a5aeb893b79949eb0000f1"""

# Shared Bit Counter

def shared_bits(a, b):
    common_bits = a & b
    count = bin(common_bits).count('1')
    return count >= 2 