"""https://www.codewars.com/kata/5266876b8f4bf2da9b000362"""

# Who likes it?

def likes(names):
    l = len(names)
    result = 'no one likes this'
    
    if l == 1:
        result = names[0] + ' likes this'
    elif l == 2:
        result = ' and '.join(names) + ' like this'
    elif l == 3:
        result = ', '.join(names[:-1]) + ' and ' + names[-1] + ' like this'
    elif l != 0:
        result = ', '.join(names[:2]) + ' and ' + str(l - 2) + ' others like this'
    
    return result