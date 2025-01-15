"""5) მომხარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ის მარტივი, თუ მარტივია დაპრინტეთ "Number is prime", სხვა შემთხვევაში "Number is not prime"(მარტივია რიცხვი, რომელიც იყოფა მარტო თავის თავზე და ერთზე)"""
#
number = int(input("Enter a number: "))
#Chack
for i in range(2, number):
    if number % i == 0:
        print("Number is not prime")