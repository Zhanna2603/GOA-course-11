"""https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python"""

# Find the missing letter

def find_missing_letter(chars):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1,len(chars)):
        if alphabet.index(chars[i]) != alphabet.index(chars[i-1])+1:
            return alphabet[alphabet.index(chars[i])-1]
        