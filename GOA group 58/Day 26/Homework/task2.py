"""2) შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)"""

def count(text):
    word_list = text.split(" ")
    for word in word_list:
        print(f"{word}{len(word)}")