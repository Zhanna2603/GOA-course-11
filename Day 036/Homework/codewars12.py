"""https://www.codewars.com/kata/520b9d2ad5c005041100000f"""

# Simple Pig Latin

def pig_it(text):
    result = []
    words = text.split()
    
    for char in words:
        if char.isalpha():
            result.append(char[1:] + char[0] +"ay")
        else:
            result.append(char)
            
    return " ".join(result)