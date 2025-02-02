"""https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python"""

# Duplicate Encoder

def duplicate_encode(word):
    word = word.lower()
    result = ""
    for i in word:
        if word.count(i) > 1:
            result += ")"
        else:
            result +="("
    return result