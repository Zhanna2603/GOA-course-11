"""https://www.codewars.com/kata/57f8ff867a28db569e000c4a"""

# Kebabize

def kebabize(st):
    res = ""
    first_char = st[0].lower()
    st = st[1:]
    st = first_char + st
    for char in st:
        if char.isdigit():
            continue
        if char.isupper():
            res +="-" + char.lower()
        else:
            res += char
    if res != "":        
        if res[0] == "-":
            return res[1:]
    return res
        