"""6) შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, გამოიყენეთ slicing-ი"""

def remove_first_and_last(chars):
    return chars[1:-1]
characters = ['a','b','c','d','e']
result = remove_first_and_last(characters)
print(result)