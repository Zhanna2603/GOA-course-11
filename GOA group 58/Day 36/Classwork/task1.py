
def manual_range(end, start = 0, step = 1):  #create a function "manual_range"with start, step and end
     while start <= end:   #the value will be executed as long as it is less than or equal to the end
        print(start)   # we output the current value of start.
        start += step  # increase the start value by the step value
    
manual_range(10, 1, 2)  #call the function



# def kebabize(st):
#     numbers_str = "0123456789"
#     result = ""
#     for i in st:
#         if i.isupper():
#             result += "-" + i.lower()
#         elif i not in numbers_str:
#             result += i
    
#     if result != "" and result[0] == "-":
#         return result[1:]


"""https://www.codewars.com/kata/5966eeb31b229e44eb00007a"""

# V A P O R C O D E

def vaporcode(s):
    s = s.replace(" ","")
    result = list(s.upper())
    return "  ".join(result)

"""https://www.codewars.com/kata/539ee3b6757843632d00026b"""

# Find the capitals


def nb_dig(n, d):
    digits = 0
    
    for i in range (n + 1):
        square = i * i
        digits = str(square * 2)
        digits += nb_dig
    return digits   
