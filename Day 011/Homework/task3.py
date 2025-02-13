"""3)Write a program that calculates the sum of a number entered by the user using a while loop."""

sum = 0
user_number = int(input("Enter number: "))

while user_number != 0:
    sum += user_number
    user_number = int(input("Enter number: "))

print("Sum of the entered numbers:", sum)