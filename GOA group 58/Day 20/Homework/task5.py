"""5) შექმენით ფუნქცია, რომელსაც გადასცემთ რიცხვების სიას. გადაუარეთ გადმოცემულ სიას for ციკლით და დააბრუნეთ ახალი სია, სადაც ჩამატებული იქნება გადმოცემული სიიდან მხოლოდ ის რიცხვები, რომლებიც მეტია 10-ზე. საბოლოოდ დააბრუნეთ ეს სია"""
def numbers_greater_than_10(numbers_list):
    new_list = []
    for number in numbers_list:
        if number > 10:
            new_list.append(number)
            return new_list
        
        numbers_list = [1, 14, 11, 8, 25, 3, 27]
        result_list = numbers_greater_than_10(numbers_list)
        print(result_list)

        #output: 14, 11, 25, 27