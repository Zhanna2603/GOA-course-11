"""3) დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული. გამოიყენეთ while loop-ი.(დაგჭირდებათ ორი ცვლადის შექმნა, ერთში შეინახავთ ჯამს, მეორეში რაოდენობას)"""
even_sum = 0
even_count = 0
num = 0 

while num <= 100:
    if num % 2 == 0:
        even_sum += num
        even_count += 1

    num += 1
average = even_sum/even_count

print("Average of even numbers from 1 to 100:", average)