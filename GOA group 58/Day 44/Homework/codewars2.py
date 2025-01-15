"""https://www.codewars.com/kata/59f08f89a5e129c543000069"""

# String array duplicates

def dup(arry):
    result = []
    for str in arry:
        new_str = ""
    previous_char = ""

    for char in str:
        if char != previous_char:
            new_str += char 
    result.append(new_str)
    return result