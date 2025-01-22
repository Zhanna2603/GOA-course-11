"""https://www.codewars.com/kata/5259b20d6021e9e14c0010d4"""

# Reverse words

def reverse_words(text):
    reverse = []
    words = text.split(" ")
    
    for i in words:
        reverse.append(i[::-1])
    return " ".join(reverse)