"""https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python"""

# Valid Braces

def valid_braces(string):
    stack = []
    nav = {")": "(", "}": "{", "]": "["}
    for i in string:
        if i in nav.values():
            stack.append(i)

        elif i in nav:
            if not stack or nav[i] != stack.pop():

                return False
             
    return not stack