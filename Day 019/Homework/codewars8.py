"""https://www.codewars.com/kata/57a2013acf1fa5bfc4000921 """

# Calculate average

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average