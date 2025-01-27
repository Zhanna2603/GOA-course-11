"""https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python"""

# Replace With Alphabet Position

def alphabet_position(text):
    result = []
    for char in text.lower():
        if char. isalpha():
            result.append(str(ord(char)-96))
    return " ".join(result)
