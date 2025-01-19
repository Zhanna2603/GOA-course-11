"""Write a function that takes a list of strings as input and returns a new list containing only the strings that start with the letter 'a'."""

def starting_with_a(strings):
    return[s for s in strings if s[0] == "a"]