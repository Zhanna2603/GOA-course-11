"""2) დაითვალეთ რამდენი ლუწი რიცხვია 1-დან 50-ის ჩათვლით(გამოიყენეთ for loop-ი)"""
even_count = 0

for i in range(1, 51):
    if i % 2 == 0:
      even_count += 1
print("Number of even numbers from 1 to 50:", even_count)