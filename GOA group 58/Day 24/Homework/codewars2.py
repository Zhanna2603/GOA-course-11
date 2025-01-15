"""https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python"""

# Highest and Lowest

def high_and_low(numbers):
    # ...
    numbers = numbers.split()
    int_nums = []
    for number in numbers:
        int_nums.append(int(number))
    max_nums = max(int_nums)
    min_nums= min(int_nums)
    
    return str(max_nums) + " " + str(min_nums)