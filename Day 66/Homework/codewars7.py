"""https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/train/python"""

# Sum a list but ignore any duplicates

def sum_no_duplicates(l):
    seen = set()
    duplicates = set()
    
    for num in l:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return sum(num for num in seen if num not in duplicates)