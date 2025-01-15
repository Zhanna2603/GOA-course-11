"""https://www.codewars.com/kata/529eef7a9194e0cbc1000255"""

# Anagram Detection

def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    
    return sorted(test) == sorted(original)



# def is_anagram(test, original):
#     return sorted(original.lower()) == sorted(test.lower()) 

