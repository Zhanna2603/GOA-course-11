"""10) შექმენით ორი ცარიელი სია, for loop-ის გამოყენებით მომხარებელს 5-ჯერ შემოატანინეთ ნებისმიერი სიტყვა. თუ შემოტანილი სიტყვის სიგრძე არ აღემატება 5-ს ჩაამატეთ პირველ სიაში, სხვა შემთხვევაში მეორეში. საბოლოოდ დაბეჭდეთ ორივე სია"""
short_words = []
long_words = []

for i in range(5):
    word = input("Enter a word: ")
    if len(word) <= 5:
        short_words.append(word)
            
    else:
        long_words.append(word)
print(short_words)
print(long_words)