"""9) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას for ციკლით და ჩაამატეთ მხოლოდ ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია"""

def filter(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
            return even_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(numbers)
print(result)

# 2, 4, 6, 8, 10