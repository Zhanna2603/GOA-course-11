"""https://www.codewars.com/kata/5656b6906de340bd1b0000ac"""

# Two to One

def longest(a1, a2):
    combined = a1 + a2
    filtered =""
    for element in combined:
        if element not in filtered:
            filtered += element 
    result = sorted(filtered)
    return "".join(result)