"""https://www.codewars.com/kata/569d488d61b812a0f7000015"""

# Data Reverse

def data_reverse(data):
    result = []
    for i in range(len(data)-8,-1,-8):
        result.extend(data[i:i+8])
    return result