"""4) შექმენით სია შემდგარი სახელებისგან. მომხარებელს შემოატანინეთ მისი სახელი, თუ მისი სახელი იქნება 5 სიმბოლოს ტოლი ან მეტი. ჩაამატეთ სიაში, სხვა შემთხვევაში დაუბეჭდეთ "Name is too short"""
names = ["Ann", "Alex", "Charlie"]
user_name = input("Enter your name: ")
if len(user_name) >= 5:
    print("Name added to the list")
else:
   print("Name is too short") 
print("Updated names list: ", names) 