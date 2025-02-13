"""Write an algorithm that checks if a given number is prime or not (prime number has only two divisors - გამყოფი) Use a for loop for this task."""

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True