"""https://www.codewars.com/kata/545a4c5a61aa4c6916000755"""

# Find the middle element

def gimme(input_array):
    middle_value = sorted(input_array)[1]
    return input_array.index(middle_value)