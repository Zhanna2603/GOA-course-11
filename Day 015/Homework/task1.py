"""Write a program that takes asks user for number (use input). If number is even, print that number is even. Else print that number is not even, also print next even number, for example if input is 15, print 16."""

num = int(input("Enter a number"))
if num % 2 == 0:
    print(num,"is even")
else:
    print(num,"is not even")
print("Next even number", num + 1)
