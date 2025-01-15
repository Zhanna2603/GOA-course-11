"""2) შექმენით რიცხვების დიაპაზონი 1-დან 100-მდე, შეამოწმეთ თუ რიცხვი იყოფა 3-ზე დაბეჭდეთ "Fizz" და გვერდზე მიუწერეთ რიცხვი. თუ რიცხვი იყოფა 5-ზე დაბეჭდეთ "Buzz" და გვერდზე მიუწერეთ რიცხვი, ხოლო თუ იყოფა 3-ზეც და 5-ზეც დაბეჭდეთ "FizzBuzz" და გვერდზე მიუწერეთ რიცხვი"""

for num in range(1, 101):
    #If it is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:

        print(f"FizzBuzz{num}")
#If divisible by 3
    elif num % 3 == 0:

        print(f"Fizz{num}")
#If divisible by 5
    elif num % 5 == 0:
        print(f"Buzz{num}")