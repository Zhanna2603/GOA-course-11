"""6) შექმენით სია, სადაც გექნებათ 1-ანები და 0-ანები, შექმენით ახალი სია, რომელიც თავიდან იქნება ცარიელი. for loop-ით გადაუარეთ პირველ სიას და თუ საიტერაციო ცვლადის მნიშვნელობა იქნება 1, ახალ სიაში ჩაამატეთ True, სხვა შემთხვევაში False. საბოლოოდ დაბეჭდეთ ახალი სია"""

old_list = [0, 0, 1, 0, 1, 1, 1, 0]
new_list = []

for i in old_list:
    if i == 1:
        new_list.append(True)
    else:
        new_list.append(False)
print(new_list)