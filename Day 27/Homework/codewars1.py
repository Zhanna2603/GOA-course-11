"""https://www.codewars.com/kata/558fc85d8fd1938afb000014"""

# Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    sorted_nums = sorted(numbers)
    return sorted_nums[0] + sorted_nums[1]