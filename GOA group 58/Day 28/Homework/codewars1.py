"""https://www.codewars.com/kata/523f5d21c841566fde000009"""

# Array.diff

def array_diff(a, b):
    result = []
    for elements in a:
        if elements not in b:
            result.append(elements)
    return result 