"""5) შექმენით რიცხვების სია, სადაც გექნებათ დუბლიკატები. გადაუარეთ მას for loop-ით და დაბეჭდეთ მხოლოდ ისეთი რცხვების ჯამი, რომლებიც არ მეორდება სიაში"""
numbers = [1, 2, 3, 4, 3, 1, 4]
unique_sum = 0
for num in numbers:
    if numbers.count(num) == 1:
        unique_sum += num 
        print("Sum of numbers without duplicates",unique_sum)