"""დავალება5) შექმენით ახალი სია. შემდეგ მომხმარებელს შეეკითხეთ მისი ასაკი და თუ ასაკი 18-ზე მეტი იქნება, შეეკითხეთ მას სახელი. მეორე ინფუთის შემდეგ სახელი შეიტანეთ სიაში და დაპრინტეთ ის.
Create a new array. Ask user his/her age and if it will be over 18, ask him/her name. Then add this name to already created array and print it."""

arr = []
age = int(input("Enter age:"))
if age > 18:
        name = int(input("Enter name:"))
        arr.append(name)
print(arr)