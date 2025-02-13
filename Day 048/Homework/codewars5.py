"""https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python"""

# Row Weights

def row_weights(array):
    t1 = 0
    t2 = 0
    for i in range(len(array)):
        if i % 2 == 0:
            t1 += array[i]
        else:
            t2 += array[i]
    return t1, t2
