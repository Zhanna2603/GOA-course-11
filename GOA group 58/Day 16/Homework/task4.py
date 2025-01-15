# 4) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი
numbers = [41, 27, -96, 38, -10]
min = numbers[0]
for i in numbers:
    if i < min:
        min = i
print("Min: ", min)