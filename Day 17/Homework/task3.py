"""Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the original list."""

def even_num_filter(numbers):
    return[num for num in numbers if num % 2 == 0]