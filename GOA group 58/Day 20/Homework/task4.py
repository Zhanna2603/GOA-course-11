"""4) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სია. ფუნქციამ უნდა დაბეჭდოს ეს სია შებრუნებულად(არ გამოიყენოთ slicing-ი)"""
def print_reverse_list(my_list):
    if len (my_list) == 0:
        return
    else:
        print(my_list[-1])
        print_reverse_list(my_list[:-1])
        my_list = [1, 2, 3, 4, 5]
        print_reverse_list(my_list)