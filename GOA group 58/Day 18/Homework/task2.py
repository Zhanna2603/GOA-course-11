"""2)  შექმენით string-ების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ სიაში არსებული ყველა სიტყვის სიმბოლოთა რაოდენობა"""
strings = [ "apple", "strawberry", "coconut", "plum"]
for w in strings:
    print(f"{w}:{len(w)}")