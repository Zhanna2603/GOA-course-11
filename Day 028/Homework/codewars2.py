"""https://www.codewars.com/kata/5208f99aee097e6552000148"""

# Break camelCase

def solution(s):
    result =""
    
    for i in s:
        if i != i.upper():
            result +=i
        else:
            result += " " + i
    return result