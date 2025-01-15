"""4) შექმენით სახელების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები, რომლებიც იწყებიან "A"-ზე"""
names = ["Anna", "Alex", "Nino", "Mariam", "Sandro","Victoria"]
for name in names:
    if name.startswith("A"):
        print(name)