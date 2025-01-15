"""3) შექმენით რიცხვების სია შემგარი 10 მინიმუმ ელემენტისგან. გაიგეთ ამ სიაში ყველაზე პატარა და დიდი რიცხვი, შემდეგ კი დაბეჭდეთ მათი ჯამი"""

num = [1, 17, -15.01, 39, 24, 8, 0.47, -63, 0, 121 ]
min_number = min(num)
max_number = max(num)

#created a variable where the sum of the min and max numbers is stored
sum = max_number + min_number
print(sum)