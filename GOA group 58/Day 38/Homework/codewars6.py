"""https://www.codewars.com/kata/5626b561280a42ecc50000d1"""

# Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for digit in range(a, b+1):
        if digit < 10:
            result.append(digit)
        else:
            sum = 0
            digit_str = str(digit)
            for i in range(len(digit_str)):
                sum += int(digit_str[i]) ** (i+1)
            if sum == digit:
                result.append(digit)
    return result