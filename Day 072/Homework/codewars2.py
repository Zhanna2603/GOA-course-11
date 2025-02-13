"""https://www.codewars.com/kata/578aa45ee9fd15ff4600090d"""

# Sort the odd

def sort_array(source_array):
    odds = []
    answer = []
    
    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")
        else:
            answer.append(i)
    odds.sort()
    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer