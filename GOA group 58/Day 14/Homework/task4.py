"""4) შექმენით სია სადაც გექნებათ 10 რიცხვი, თქვენი დავალებაა გაიგოთ ამ სიაში ყველა ლუწი და კენტი რიცხვიოს ჯამი და დაბეჭდოთ"""
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = 0
odd_num = 0

for number in num:
    if number % 2 == 0:
        even_num += number
    else:
        odd_num += number
print("Even sum " + str(even_num))

print("Odd sum " + str(odd_num))