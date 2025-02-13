"""https://www.codewars.com/kata/5938f5b606c3033f4700015a/train/python"""

# Alphabet war - airstrike - letters massacre

def alphabet_war(fight):
    result = ""
    new_fight = "|" + fight + "|"
    
    for char in range (1, len(new_fight) - 1):
        if new_fight [char + 1] == "*":
            continue
        if new_fight [char - 1] == "*":
            continue
            
        result += new_fight[char]
    
    left = {"w":4,"p":3,"b":2,"s":1,}
    right = {"m":4,"q":3,"d":2,"z":1,}
    
    left_score = 0
    right_score = 0

    for i in result:
        if i in left:
            left_score += left[i]
        elif i in right:
            right_score += right[i]
            
    if left_score < right_score:
        return "Right side wins!"
    elif left_score > right_score:
        return "Left side wins!"
    else:
        return "Let's fight again!"