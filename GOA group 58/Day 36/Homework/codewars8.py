"""https://www.codewars.com/kata/5264d2b162488dc400000001"""

# Stop gninnipS My sdroW!

def spin_words(sentence):
    words = sentence.split(" ")
    result = []
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result)