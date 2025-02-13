"""Ask user for whole number. Then create a factorial for this number and print it out (If you don't know what a factorial is, google it)."""

num = int(input("Enter a number:"))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial) 