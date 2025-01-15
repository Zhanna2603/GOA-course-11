"""https://www.codewars.com/kata/517abf86da9663f1d2000003"""

# Convert string to camel case

def to_camel_case(text):
    text = text.replace("-","_")
    text = text.split("_")
    res = text[0]
    for i in range(1, len(text)):
        res += text[i].capitalize()
    return res