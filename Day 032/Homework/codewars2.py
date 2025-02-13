"""https://www.codewars.com/kata/52449b062fb80683ec000024"""

# The Hashtag Generator

def generate_hashtag(s):
    if not s:
        return False
    s = s.title()
    splited_str = s.split()
    str = "#"
    for i in splited_str:
        str += i
    result = "".join(str)
    if len(str)>140:
        return False
    return result