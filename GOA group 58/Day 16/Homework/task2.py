# 2) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი
numbers = [20, 0, -7, 81, 34]
max_numbers = numbers [0]
for number in numbers:
    if number > max_numbers:
        max_numbers = number        
print("Max: ",max_numbers)