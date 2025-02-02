"""https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python"""

# Sentence Smash

def smash(words):
    sentence = ""
    for i, word in enumerate(words):
        if i > 0: 
            sentence += " "
        sentence += word
    return sentence