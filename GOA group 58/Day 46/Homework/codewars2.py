"""https://www.codewars.com/kata/5959ec605595565f5c00002b"""

# Reverse the bits in an integer

def reverse_bits(n):
    binary_n = bin(n)[2:]
    reversed_binary_n = binary_n[::-1]
    reversed_n = int(reversed_binary_n, 2)
    return reversed_n