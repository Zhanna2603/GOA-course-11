"""https://www.codewars.com/kata/5813d19765d81c592200001a"""

# Don't give me five!

def dont_give_me_five(start,end):
    result = []
    for i in range(start, end+1):
        if "5"in str(i):
            continue
        else:
            result.append(i)
    return len(result)



