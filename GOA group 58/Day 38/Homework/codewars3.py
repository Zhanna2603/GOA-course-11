"""https://www.codewars.com/kata/56582133c932d8239900002e"""

# Find Count of Most Frequent Item in an Array

def most_frequent_item_count(collection):
    if not collection: 
        return 0
    frequency = {}
    for num in collection:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return max(frequency.values())