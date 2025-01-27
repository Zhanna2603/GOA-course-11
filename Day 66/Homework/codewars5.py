"""https://www.codewars.com/kata/61c78b57ee4be50035d28d42/train/python"""

# Merge overlapping strings

def merge_strings(first, second):
    overlap_length = min(len(first), len(second))
    
    for i in range(overlap_length, 0, -1):
        if first[-i:] == second[:i]:
            return first + second[i:]
    return first + second