"""https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3"""

# Abbreviate a Two Word Name

def abbrevName(name):
    first_initial = name[0]
    for letter in range(len(name)):
        if name[letter]  == " ":
            last_initial = name[letter + 1]
    return (first_initial.upper() + "." + last_initial.upper())