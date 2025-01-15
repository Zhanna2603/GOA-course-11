# task1
# 1)
def in_asc_order(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# 2)
def in_asc_order(arr):
    sorted_list = arr.copy()
    sorted_list.sort()

    for i in range(len(arr)):
        if sorted_list[i] != arr[i]:
            return False
    return True 


# task2

def valid_braces(string):
    stack = []
    nav = {")": "(", "}": "{", "]": "["}
    
    for i in string:
        if i in nav.values():
            stack.append(i)

        elif i in nav:
            if not stack or nav[i] != stack.pop():

                return False      
    return not stack
    

# task3
def expanded_form(num):
    result = []
    num= str(num)
    for i in range(len(num)):
        if num[i] != "0":
            result.append(num[i] + "0" * (len(num) - i))
    return "+".join(result)







