"""https://www.codewars.com/kata/56747fd5cb988479af000028/train/python"""

# Get the Middle Character

def get_middle(s):
    s_len = len(s)
    middle_char = s_len // 2
    if s_len % 2 == 0:
        return s[middle_char -1:middle_char +1 ]
    return s[middle_char]