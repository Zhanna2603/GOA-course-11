"""https://www.codewars.com/kata/59cfc000aeb2844d16000075"""

# Alternate capitalization

def capitalize(s):
    even_capitalization = ""
    odd_capitalization = ""
    for i,char in(s):
        if i % 2 == 0:
            even_capitalization += char.upper()
        else:
            even_capitalization += char
        if i % 2 != 0:
            odd_capitalization += char.upper()
        else:
            odd_capitalization += char
    return [even_capitalization, odd_capitalization]