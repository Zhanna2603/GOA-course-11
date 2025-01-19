"""Write a program that asks the user to enter a number and then prints whether the number is positive, negative, or zero using an if-else statement."""

number = int(input("Enter a number: "))

if number > 0:
    print("This is a positive number")
elif number < 0:
    print("This is a negative number")
else:
    print("This is a zero")