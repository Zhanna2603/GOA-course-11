"""4)მომხარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ ის, რომელიც არის მეტი. თუ ორივე რიცხვი ტოლია დაბეჭდეთ "Both numbers are equal"""

#Enter 2 numbers
num1 = input(int())
float(input("Enter the first number: "))
num2 = input(int())
float(input("Enter the stcond number: "))

#Comparint of numbers
if num1 > num2:
    print("The first number is more: " , num1)

elif num1 == num2:
    print("They are equal: " , num1 , num2)

else:
    print("The first second is more: " , num2)

