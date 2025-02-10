"""https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python"""

# Bouncing Balls

def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window:
            count += 1
    return count