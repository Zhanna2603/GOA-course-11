"""https://www.codewars.com/kata/5a53a17bfd56cb9c14000003"""

# Disarium Number (Special Numbers Series #3)

def disarium_number(number):
    digits = str(number)
    sum = 0
    for i in range(len(digits)):
        sum += int(digits[i]) ** (i + 1)
    if sum == number:
        return "Disarium !!"
    else:
        return "Not !!"