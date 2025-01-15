"""5)მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ შემოტანილი რიცხვის ფაქტორიალი(დასერჩეთ რა არის ფაქტორიალი)
"""

number = int(input("Enter a number: "))
product = 1
for i in range(1, number + 1):
    product *= i
print(product)