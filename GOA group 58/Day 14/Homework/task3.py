"""3) შექმენით სახელების სია სადაც გექნებათ მინიმუმ 10 სახელი, დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები რომლების ინდექსებიც არის ლუწი"""
names = ["Noah","Liam","William","Mason","James","Benjamin","Jacob", "Michael"]
for i in range(len(names)):
    if i % 2 == 0:
        print(names[i])