"""3) შექმენით რიცხვების სია, while loop-ის გამოყენებით გაიგეთ ამ სიაში ყველა ლუწი რიცხვის ჯამი და დაპრინტეთ"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
even_sum = 0
while i < len(numbers):
    if numbers [i] % 2 == 0:    
        even_sum += numbers[i]
    i += 1
    print("Even numbers sum:", even_sum)