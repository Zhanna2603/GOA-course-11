"""10) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია"""


# filter numbers by n

def name(names):
    filter = []
    for i in names:
        if name.startswith("N"):
            filter.append(i)
            return filter
names = ["Nino","Anna","Nana","Mariam"]
result = filter(names)
print(result)

# Nino, Nana