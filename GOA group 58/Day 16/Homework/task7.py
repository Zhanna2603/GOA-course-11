# 7) შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება
symbols = ["a", "b", "c", "f", "a", "c"]
unique_symbols = []
for symbol in symbols:
    if symbol not in unique_symbols:
        unique_symbols.append(symbol)
print("Unique symbols:",unique_symbols)