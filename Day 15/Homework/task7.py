"""Implement a simple calculator that takes two numbers and an operator (+, -, *, /) as input from the user and performs the corresponding operation. Bonus task if you want, it's not necessary - add degree (ხარისხი), use ** operator for it."""

def calculator(x, y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        return x / y
    elif operation == "**":
        return x ** y
    else:
        return "Invalid operation"