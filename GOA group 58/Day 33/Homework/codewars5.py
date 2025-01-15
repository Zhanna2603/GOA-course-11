"""https://www.codewars.com/kata/57f609022f4d534f05000024"""

# Find the stray number

def stray(arr):
    for i in range(len(arr)):
        if arr[0] != arr[1] and arr[0] != arr[2]:
            return arr[0]
        if arr[0] != arr[i]:
            return arr[i]