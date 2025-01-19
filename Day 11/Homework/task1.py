"""1) Write a program that takes an input from the user and checks if it's a positive, negative, or zero number using if-else."""

number = int(input("Enter a number: "))

if number > 0:
    print("This is a positive number")
elif number < 0:
    print("This is a negative number")
else:
    print("This is a zero")