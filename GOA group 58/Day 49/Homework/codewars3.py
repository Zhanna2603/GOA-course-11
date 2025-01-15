"""https://www.codewars.com/kata/557a2c136b19113912000010"""

# reverseIt

def reverse_it(data):
    if type(data) == str:
        return data[::-1]
    elif type(data) == int:
        return int(str(data)[::-1])
    elif type(data) == float:
        return float(str(data)[::-1])
    return data