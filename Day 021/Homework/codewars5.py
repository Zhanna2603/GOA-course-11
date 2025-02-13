"""https://www.codewars.com/kata/5467e4d82edf8bbf40000155"""

# Descending Order

def descending_order(num):
    number = str(num) ; 
    result = '' ; 
    for i in range (0,len(number)) : 
        if number[i] == '9' : 
            result = result + '9' ; 
    for i in range (0,len(number)) : 
        if number[i] == '8' : 
            result = result + '8' ; 
    for i in range (0,len(number)) : 
        if number[i] == '7' : 
            result = result + '7' ; 
    for i in range (0,len(number)) : 
        if number[i] == '6' :
            result = result + '6' ; 
    for i in range (0,len(number)) : 
        if number[i] == '5' : 
            result = result + '5' ; 
    for i in range (0,len(number)) : 
        if number[i] == '4' : 
            result = result + '4' ; 
    for i in range (0,len(number)) : 
        if number[i] == '3' : 
            result = result + '3' ; 
    for i in range (0,len(number)) : 
        if number[i] == '2' : 
            result = result + '2' ; 
    for i in range (0,len(number)) : 
        if number[i] == '1' : 
            result = result + '1' ; 
    for i in range (0,len(number)) : 
        if number[i] == '0' : 
            result = result + '0' ;
            
    return int(result)