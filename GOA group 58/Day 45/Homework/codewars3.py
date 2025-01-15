"""https://www.codewars.com/kata/52a112d9488f506ae7000b95"""

# Is Integer Array?

def is_int_array(arr):
    if not isinstance(arr,(list,tuple)):
        return False 
    if arr == []:
        return True 
    for element in arr:
        if not isinstance(element,int):
            if not isinstance(element,float) or not element.is_integer():
                return False
    return True
