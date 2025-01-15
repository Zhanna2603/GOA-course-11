"""2) შექმენით პროგრამა while ციკლის საშვალებით რომელიც გამოთვლის ყველა ნატურალური რიცხვის ჯამს 1-იდან 50-მდე"""
sum_num = 0
num = 1
while num <= 50:
    sum_num += num
    num += 1

    print("The sum of all the numbers from 1 to 50: " , sum_num)