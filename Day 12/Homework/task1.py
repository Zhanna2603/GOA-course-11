"""Calculate the sum of all even numbers from 1 to 10 using a while loop:"""

num = 1
sum = 0
while num <= 10:
    if num % 2 == 0:
        sum += num
    num += 1
print(sum)