"""https://www.codewars.com/kata/585a033e3a36cdc50a00011c"""

# Frequency sequence

def freq_seq(s, sep):
    result = ""
    for i in s:
        count = str(s.count(i))
        result += count + sep
    return result [:-1]