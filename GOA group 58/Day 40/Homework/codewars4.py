"""https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python"""

# Highest Scoring Word

def high(x):
    splited_x = x.split()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    result = ""
    max_score = 0
    
    for i in splited_x:
        score_sum = 0
        
        for x in i:
            score_sum += alphabet.index(x) + 1
        if score_sum > max_score:
            result = i
            max_score = score_sum
    return result