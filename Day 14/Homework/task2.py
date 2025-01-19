"""დავალება2) შექმენით ახალი სია, რომელშიც შეიტანთ ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.
Create a new array, which will include even numbers from the first array. Then print this new array."""

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_num = []
for num in arr:
    if num % 2 == 0:
        even_num.append(num)
print(even_num)