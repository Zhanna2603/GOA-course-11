"""https://www.codewars.com/kata/5375f921003bf62192000746/train/python"""

# Word a10n (abbreviation)

def abbreviate(s):
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i].isalpha():
            start = i
            while i < n and s[i].isalpha():
                i += 1
            word = s[start:i]
            if len(word) >= 4:
                abbreviated = f"{word[0]}{len(word) - 2}{word[-1]}"
                result.append(abbreviated)
            else:
                result.append(word)
        else:
            result.append(s[i])
            i += 1
    
    return ''.join(result)