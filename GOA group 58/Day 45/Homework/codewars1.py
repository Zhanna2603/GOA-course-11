"""https://www.codewars.com/kata/525f47c79f2f25a4db000025"""

# Valid Phone Number

def valid_phone_number(phone_number):
    
    if len(phone_number) != 14:
        return False
    
    if phone_number[0] != "(" or phone_number [4] != ")":
        return False
    
    for i in range(1,4):
        if not phone_number[i].isdigit():
            return False 
        
    if phone_number[5] != " ":
        return False
    
    for i in range (6,9):
        if not phone_number[i].isdigit():
            return False 
    
    if phone_number[9] != "-":
        return False
    
    for i in range(10, 14):
        if not phone_number[i].isdigit():
            return False
        
    return True 
