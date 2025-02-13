"""https://www.codewars.com/kata/514a6336889283a3d2000001/train/python"""

# JavaScript Array Filter

def get_even_numbers(arr):
    a = []
    for i in range(0,len(arr)):
        if arr[i] % 2 != 0:
            a.append(arr[i])
    for i in range(0,len(a)):
        arr.remove(a[i])
    return arr