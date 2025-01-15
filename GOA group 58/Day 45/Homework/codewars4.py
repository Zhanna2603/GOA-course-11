"""https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f"""

# Twisted Sum

def compute_sum(n):
    sum = 0
    for i in range(1, n+1):
        num = i
        while num > 0:
            sum += num % 10
            num = num // 10
    return sum