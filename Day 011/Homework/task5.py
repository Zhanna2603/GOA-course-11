"""5)Write a program that simulates a simple login system. Ask the user for a username and password, and if they enter "admin" and "password123", respectively, print "Login successful" using if-else."""

username = input("Enter user's name: ")
password = input("Enter password: ")

if username == "admin" and password == "password123":
    print("Login Successful!")
else:
    print("Incorrect username or password")