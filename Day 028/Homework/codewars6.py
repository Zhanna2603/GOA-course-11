"""https://www.codewars.com/kata/583f158ea20cfcbeb400000a"""

# Make a function that does arithmetic!

def arithmetic(a, b, operator):
    if operator == "add":
        return a+b
    elif operator == "subtract":
        return a-b
    elif operator == "multiply":
        return a*b
    elif operator == "divide":
        return a/b
    else:
        return "Bug"