"""https://www.codewars.com/kata/54ff3102c1bad923760001f3"""

# Vowel Count

def get_count(sentence):
    vowels = ["a","e","i","o","u"]
    count = 0
    for vowel in vowels:
        for char in sentence:
            if char == vowel:
                count += 1
    return count