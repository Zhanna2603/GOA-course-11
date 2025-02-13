"""https://www.codewars.com/kata/52bc74d4ac05d0945d00054e"""

# First non-repeating character

def first_non_repeating_letter(s):
    lower = s.lower()
    for i in s:
        if lower.count(i.lower()) == 1:
            return i
    return ""