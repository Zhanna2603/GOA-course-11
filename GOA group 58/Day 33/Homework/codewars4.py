"""https://www.codewars.com/kata/51f2b4448cadf20ed0000386"""

# Remove anchor from URL

def remove_url_anchor(url):
    res = ""
    for char in url:
        if char != "#":
            res += char
        else:
            break
    return res