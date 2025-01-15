"""https://www.codewars.com/kata/541c8630095125aba6000c00"""

# Sum of Digits / Digital Root

def digital_root(n):
    if len(str(n)) == 1:
        return n
    num = n
    result = num
    while len(str(result)) != 1:
        num = 0
        for i in str(result):
            num += int(i)
        result = num
    return result