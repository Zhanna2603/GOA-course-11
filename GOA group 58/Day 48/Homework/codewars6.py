"""https://www.codewars.com/kata/58cda88814e65627c5000045"""

# Write Number in Expanded Form - Part 2

def expanded_form(num):
    result = ""
    num = str(num)
    section = num.split(".")
    floats = section[1]
    wholes = section[0]
    
    for i in range(len(wholes)):
        if int(wholes[i]) != 0:
            relevance = int(wholes[i]) * (10**len(wholes[i:]))
            relevance = int(relevance/10)
            result += str(relevance) + " + "
            
    for i in range (len(floats)):
        if int(floats[i])!= 0:
            result += f"{floats[i]}/{10** (1 + len(floats[:i]))} + "
            
    return result[:-3]