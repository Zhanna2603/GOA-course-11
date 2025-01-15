"""https://www.codewars.com/kata/56d02e6cc6c8b49c510005bb"""

# Find missing numbers

def find_missing_numbers(arr):
    if len(arr) <= 1:
        return []
    miss_num = []
    for i in range(arr[0], arr[-1]):
        if i not in arr:
            miss_num.append(i)
    return miss_num