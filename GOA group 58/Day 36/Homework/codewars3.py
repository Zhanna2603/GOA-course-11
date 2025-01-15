"""https://www.codewars.com/kata/566fc12495810954b1000030/train/python"""

# Count the Digit

def nb_dig(n, d):
    count = 0
    for i in range(0, n + 1):
        squared_num = i ** 2
        count += str(squared_num).count(str(d))
    return count