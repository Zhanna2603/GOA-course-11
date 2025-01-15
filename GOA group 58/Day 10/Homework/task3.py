"""3)while ციკლის გამოყენებით გამოიტანეთ 1-დან 20-მდე ყველა კენტი რიცხვის ჯამი"""
#Initial value
num = 1
total_sum = 0

#summation of add numbers
while num <= 20:
    if num % 2 != 0:
        total_sum += num
        num += 1
#outcome
        print("The sum of all add numbers: " , total_sum)