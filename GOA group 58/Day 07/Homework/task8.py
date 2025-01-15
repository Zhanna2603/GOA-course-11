"""8) მომხარებელს შემოატანინეთ მისი ასაკი და სახელი, შემდეგ შეამოწმეთ არის თუ არა ის სრულწლოვანი და უდრის თუ არა მისი სახელი თქვენს სახელს"""

# The user's name and age
age = int(input("Enter your age: "))
name = int(input("Enter your name: "))

#Checking of full age
if age >= 18:
    print("You're an adult: ")
else:
    print("You're not an adult: ")

#Checking :users name == Zhanna?
if name == "Zhanna":
    print("The name is identical: ")
else:
    print("The name is not identical: ")