"""6) მომხარებელს შემოატანინეთ მისი ასაკი, როგორც სტრინგი და დაბეჭდეთ მისი ტიპი. შემდეგ შეუცვალეთ მას მონაცემთა ტიპი ჯერ integer-ად, შემდეგ float-ად (ყოველ გარდაქმნაზე დაბეჭდეთ შედეგი)"""

age = input("Enter your age: ")
print("The original data type: ", type(age))

age_integer = int(age)
print("Age as integral number: ", (age))
print("The integral data type: ", type(age_integer))

age_float = float(age)
print("Age as floating point number: ", (age_float))
print("The floating point data type: ", type(age_float))
