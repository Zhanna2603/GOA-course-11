"""Write a function that takes a list of strings as input and returns a new list containing only the strings that have a length greater than 5."""

def len_filter(strings):
    return[string for string in strings if len(strings) > 5]