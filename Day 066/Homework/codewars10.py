"""https://www.codewars.com/kata/5a491f0be6be389dbb000117/train/python"""

# Drinking Game

def game(a, b):
    import math
    if a < 1 or b < 1:
        return "Non-drinkers can't play"
    
    m = math.isqrt(a) + 1
    mike_step = 2 * m - 1

    j = (math.isqrt(4 * b + 1) - 1) // 2 + 1
    joe_step = 2 * j
    
    return "Joe" if mike_step < joe_step else "Mike"