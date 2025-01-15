"""https://www.codewars.com/kata/54bb6f887e5a80180900046b"""

# longest_palindrome

def longest_palindrome (s):
    length = []
    n = len(s)
    for i in range(len(s)):
        for j in range (i + 1, n+ 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                length.append(len(sub))
    if len(s)!= 0:
        return max(length)
    else:
        return 0
