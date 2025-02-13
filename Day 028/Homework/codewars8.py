"""https://www.codewars.com/kata/515f51d438015969f7000013"""

# Pyramid Array

def pyramid(n):
    list = []
    for i in range (1, n+1):
        list.append(i *[1])
    return list