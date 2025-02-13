"""https://www.codewars.com/kata/5842df8ccbd22792a4000245"""

# Write Number in Expanded Form

def expanded_form(num):
    result = []
    num= str(num)
    for i in range(len(num)):
        if num[i] != "0":
            result.append(num[i] + "0" * (len(num)-i-1))
    return " + ".join(result)