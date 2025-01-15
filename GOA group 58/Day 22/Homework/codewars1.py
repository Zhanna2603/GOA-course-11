"""https://www.codewars.com/kata/546e2562b03326a88e000020/solutions?filter=me&sort=best_practice&invalids=false"""

# Square Every Digit

def square_digits(num):
    # Your code here
    num = str(num)
    res =""
    for digit in num:
        res += str(int(digit)**2)
    return int(res)