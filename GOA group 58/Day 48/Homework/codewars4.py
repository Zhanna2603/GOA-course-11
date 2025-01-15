"""https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9"""

# +1 Array

def up_array(arr):
    if len(arr) == 0: return None
    
    string1 = ""
    
    for i in arr:
        if i < 0 or len(str(i)) > 1:
            return None
        else:
            string1 += str(i)

    if string1[0] == "0" and len(str(int(string1) + 1)) < len(arr):
        str1 = "0" + str(int(string1) + 1)
    else:
        str1 = str(int(string1) + 1)
    
    result = []
    
    for i in str1:
        result.append(int(i))
        
    return result