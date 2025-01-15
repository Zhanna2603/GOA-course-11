"""https://www.codewars.com/kata/55908aad6620c066bc00002a"""

# Exes and Ohs

def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")