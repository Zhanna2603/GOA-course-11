"""https://www.codewars.com/kata/59824f384df1741e05000913/train/python"""

# Most common first

def most_common(s):
    st = ""
    count = 1
    while len(st) < len(s):
        sub = ""
        for c in s:
            if s.count(c) == count:
                sub += c
        st  = sub + st
        count+=1 
    return st