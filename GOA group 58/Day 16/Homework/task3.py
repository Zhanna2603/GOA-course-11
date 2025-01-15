# 3) შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი
numbers = [7, 1, 9]
for number in numbers:
    product = 1
    for i in range (2, number + 1):
        product *= i
        print (product)