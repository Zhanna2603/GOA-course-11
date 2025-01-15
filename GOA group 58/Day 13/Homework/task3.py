"""3) შექმენით ხილების სია, სადაც გექნებათ მინიმუმ 3 ელემენტი. მომხარებელს შემოატანინეთ თავისი საყვარელი ხილი, თუ სიის ბოლო ელემენტის ინდექსი არის ლუწი ჩაამატეთ შემოტანილი ხილი სიაში, სხვა შემთხვევაში არ ჩაამატოთ """
fruits = ["mandarin", "blueberry", "fig"]
user_fruit = input("Enter your favorit fruit: ")
if (len(fruits)-1) % 2 == 0:
    fruits.append(user_fruit)
    print("Fruit has been added to the list")
else:
  if (len(fruits)-1) % 2 == 0:
    print("Fruit was not added to the list")
print("Updated fruits list", fruits)