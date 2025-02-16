"""1) გააკეთეთ 10-10 მაგალითი  while, for and if-else ზე"""

# Examples of for loop:

for x in range(1, 7):
    print(x)


for i in reversed(range(1, 11)):
    print(i)
print("Happy New Year!")


for words in ("Luna"):
    print(words)


for m in range(1, 21):
    if m == 13:
        continue
    else:
        print(m)


# Some examples of nested loops

for z in range (3):
    for y in range(9):
        print(y, end = "-")


while x > 0:
    for y in range(4):
        print("Nested Loop №2")


for x in range(5):
    while y > 0:
        print("Nested Loop №3")


for x in range(1, 9):
    print(x, end = "")      # to print everything in one line


list1 = [1, 2, 3]
list2 = [4, 5, 6,]

for i in list1:
    for j in list2:
        print(i, j)
    print()


numbers_divisible_by_three = [3, 6, 9, 12, 15]

for num in numbers_divisible_by_three:
    quotient = num / 3
    print(f"{num} divided into three {int(quotient)}.")


# Examples of while loop:

a = 5 
while a > 0:
    print(a, end = " ")
    a -= 1


i = 1
while i <= 10:
    print(i)
    i += i
else:
    print("Cicle is over")


n = int(input("Enter number"))
a = 0 
while n > 0:
    a = a + n % 10
    n = n // 10
print("Sum of numbers", a)


a = 1
while a == 1:
    b = input("What's your name?")
    print("Hi,", b)


a = 1
while a < 5:
   print("True")
   a = a + 1
else:
   print("False")


a = 1
while a < 5:
    a += 1
    if a == 3:
	    break
print(a) # 2


a = 1
while a < 5:
    a += 1
    if a == 3:
	    continue
print(a)  # 2, 4, 5


i = 0  
str1 = "Niniko"
  
while i < len(str1):   
    if str1[i] == "i":
        i += 1  
        continue  
    print('Current Letter :', a[i])   
    i += 1


str1 = "javascript"
i = 0  
  
while i < len(str1):   
    i += 1  
    pass  
print("Value of i :", i)


i=1  
while(i<=10):    
    print(i)   
    i=i+1


# Examples of if else loop:

n = 100
if n > 10:
     print("n v 10")

x = 10
if x > 5:
    print("x more than 5")


weather = "sunny"
if weather == "sunny":
    print("It's sunny today!")
else:
    print("There's sunny today!")


score = 75
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
elif score >= 60:
    print("You got an D!")
else:
    print("You are failed!")


age = 20
if age >= 18:
    print("You are adult")
else:
    print("You are child")


a = 1
if a < 0:
    print("Negative number")
else:
    print("Positive number")


score = int(input())
if score >= 75:
    print("You are passed!")
else:
    print("You are failed!")


bun = 35
pie = 50
money = int(input("How much money do you have?"))

if money >= 50:
  print("You can buy 1.5 kilos of apples")
else:
  print("You can't buy 1.5 kilos of apples, but you can buy a glass of barberries.")


x = 7
y = 8
if x > 5 and y > 5:
    print("x and y more 5")
if x > 5 or y > 10:
    print("x more than 5 or y more 10")
if not x < 5:
    print("x not less than 5")


radius = int(input("Enter radius: "))

if radius >= 0:
    print("Circumference = ",  2  *  3.14  *  radius)
    print("Area = ", 3.14 * radius ** 2)
else:
    print("Please, enter a positive number")