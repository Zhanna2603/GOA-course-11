"""8) მომხმარებელს შემოატანინეთ რიცხვი 1-დან 100-ის ჩათვლით(ეს იქნება მისი ქულა). თუ მაგალითად 90-დან 100-ის ჩათვლით ექნება ქულა გამოუტანეთ "Your grade is A", თუ 80-დან 90-მდე, გამოუტანეთ "Your grade is B", თუ 70-დან 80-მდე გამოუტანეთ "Your grade is C", სხვა შემთხვევაში გამოუტანეთ "Your grade is D"""
score = int(input("Enter your score (1-100): "))
if 90 <= score <= 100:
    print ("Your grade is A")
elif 80 <= score <= 90:
    print("Your grade is B")
elif 70 <= score <= 80:
    print("Your grade is C")
else:
    print("Your grade is D")
