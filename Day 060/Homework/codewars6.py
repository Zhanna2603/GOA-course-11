"""https://www.codewars.com/kata/54fb963d3fe32351f2000102/train/python"""

# Collatz Conjecture Length

def collatz(n):
    length = 1  
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length
