"""5) შექმენით სია შემდგარი 10 ელემენტისგან. დაპრინტეთ ის და მომხარებელს შემოატანინეთ რიცხვი 1-დან 10-ჩათვლით. შემდეგ წაშალეთ სიის ის ელემენტი რომელი რიცხვიც გადმოგეცათ და დაპრინტეთ განახლებული სია"""

my_list = ["apple", "orange", "pear", "cherry", "banana","kiwi", "grape", "plum", "fig", "blueberry"]
print("List: ",my_list)

index = int(input("Enter a number (1-10): "))
del my_list[index]
print(my_list)
