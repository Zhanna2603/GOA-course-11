"""https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5"""

# Reverse a Number

def reverse_number(n):
    if n < 0 :
        n = str(n)
        n = n[1::]
        n = int(n[::-1])
        return -n
    else:
        n = str(n)
        n = n[::-1]
        return int(n)