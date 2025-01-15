"""https://www.codewars.com/kata/5d5ee4c35162d9001af7d699"""

# Sum of Minimums!

def sum_of_minimums(numbers):
    row_minimums = [min(row) for row in numbers]
    return sum(row_minimums)