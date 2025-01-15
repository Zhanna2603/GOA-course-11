"""6) დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია"""
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
