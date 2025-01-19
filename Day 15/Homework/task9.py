"""Using for loop, ask user for number. Then create a list which will have even numbers in next range: from 0 to user's number. At last, print out whole list. """

user_num = int(input("Enter a number:"))
even_num = []
for i in range(0, user_num + 1):
    if i % 2 == 0:
        even_num.append(i)
print("List of even numbers from 0 to", user_num, ":", even_num)