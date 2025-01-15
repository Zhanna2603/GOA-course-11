"""8) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას while ციკლით და ჩაამატეთ გაორმაგებული რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია"""

def double_numbers(numbers):
    double_list = []
    i = 0
    while i < len(numbers):
        double_list.append(numbers * 2)
        return double_list
    numbers = [1, 2, 3, 4]
    