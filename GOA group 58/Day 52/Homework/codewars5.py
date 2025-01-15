"""https://www.codewars.com/kata/55688b4e725f41d1e9000065"""

# Even Fibonacci Sum

def even_fib(n):
    a, b = 0, 1
    even_sum = 0

    while b < n:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    
    return even_sum