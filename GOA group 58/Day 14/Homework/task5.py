"""5) შექმენით სია სადაც გექნებათ 10 რიცვი, შემდეგ შექმენით ახალი სია, სადაც ჩაამატებთ პირველი სიიდან ყველა ლუწ რიცხვს და გაიგებთ მათ საშუალო არითმეტიკულს.(ახალ სიაზე გამოიყენეთ len() ფუნქცია)"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

sum = 0
count = 0

for number in even_numbers:
    sum += number
    count += 1 

average = sum/count
print(average)
