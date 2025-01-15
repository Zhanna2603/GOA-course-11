# 5) შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები, შემდეგ შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).
numbers = [25, -3, 71, 1, -49]
negatives = []
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        negatives.append(numbers[i])
    i += 1
print(negatives)
        