"""6)მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში. შემდეგ დაბეჭდეთ შემოტანილი რიცხვის ჩათვლით ყველა რიცხვის კვადრატის ჯამი"""
num = int(input("Enter a number: "))
sum = 0
for i in range (1, num + 1):
    sum += i 
print(sum)