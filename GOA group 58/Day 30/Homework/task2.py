"""2) შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია"""

my_list = [1, 2, 3, 4, 5]
del my_list[2] # delete the third element 
my_list.insert(0, 6)  # using the "insert" function added new element to the zero position
print(my_list)

# insert is used to add new element to the particular position of the list
# At first we must write the position and then the element