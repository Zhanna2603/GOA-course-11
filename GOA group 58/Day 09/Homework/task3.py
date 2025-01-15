"""3) შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) მანამდე სანამ არ შეიყვანს 1234-ს"""

pin = 1234
code = int(input("Enter PIN code: "))
while pin != code:
   code = int(input("Enter PIN code: "))