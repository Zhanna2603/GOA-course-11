"""6) Write a program that asks the user for their age and prints a message based on the age range (e.g., "Child", "Teenager", "Adult") using if-elif-else."""

age = int(input("Enter age: "))

if age < 18:
    print("Child")
elif 18 <= age < 60:
    print("Adult")
else:
    print("Pensioner")