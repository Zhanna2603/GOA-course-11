1) შექმენით ფუნქიცა, manual_find, რომელსაც გადაეცემა არგუმენტად სთრინგიმ და ერთი სიმბოლო, რომელიც უნდა ვიპოვოთ ამ სთრინგში.

2) შექმენით ფუნქცია manual_count, რომელსაც არგუმენტად გადაეცემა რიცხვბის სია, და ერთი რიცხვი, რომლის რაოდენობაც უნდა ვიპოვოთ ამ სიაში. დააბრუნეთ მიღებული რაოდენობა


# def manual_find(meaing):
#       for i in range(len(meaing)):
#         if meaning == 
#       return i
# print (manual_find)


def manual_find(word, symbol):
    if symbol not in word:
        return -1
    
    index = 0
    
    for i in word:
        if i == symbol:
            return index
        index +=1

print(manual_find("nika","a"))

