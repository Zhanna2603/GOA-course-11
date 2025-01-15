#1) შექმენით რიცხვების სია, შემდგარი მინიმუმ 10 ელემენტისგან. გადაუარეთ ამ საის while loop-ის გამოყენებით. გაიგეთ ცალკე ლუწი და კენტი რიცხვების ჯამი, საბოლოოდ შეადარეთ ისინი ერთმანეთს და დაპრინტეთ უდიდესი
#list of numbers
numbers = [10, 15, 23, 42, 51, 64, 73, 88, 91, 102]

even_sum = 0
odd_sum = 0

#index for the while loop 
index = 0

while index < len(number):
    if numbers[index]%2 == 0:
       even_sum += numbers[index]
else:
       odd_sum += numbers[index]
       index += 1

    #Compare
    if   even_sum > odd_sum:
        print("The largest sum is the even sum", even_sum)
    elif odd_sum > even_sum:
         print("The largest sum is the even sum", odd_sum)
    else: 
        print("Both sums are equal:even_sum")



# 2) შექმენით სიმბოლოების სია, გადაუარეთ მას for loop-ით და სიიდან ყველა სიმბოლოს შორის მოახდინეთ კონკადინაცია. ციკლის გარეთ დაგჭირდებათ ცვლადი სადაც შაამატებთ ამ სთრინგებს
# კონკადინაცია - სტრინგის, სტრინგზე დამატებე(შეერთება)
numbers = [4,5,2,8,12,32,44,18,20]
index = 0
even_sum = 0
odd_sum = 0

while index != len(numbers):
    if numbers[index] % 2 == 0:
        even_sum += numbers[index]
    else:
        odd_sum += numbers[index]
    index += 1


if even_sum > odd_sum:
    print(even_sum)
else:
    print(odd_sum)