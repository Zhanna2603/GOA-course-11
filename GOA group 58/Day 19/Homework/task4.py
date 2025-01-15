"""4) შექმენით ცვლადი სადაც შეინახავთ სთრინგს და გაიგეთ, არის თუ არა ის პალინდრომი(პალინდრომი არის ისეთი სიტყვა, რომელიც ორივე მხრიდან ერთნაირად იკითხება, მაგალითად, "ana"...)"""

word = input("Enter a word: ")
reversed_word = word[::-1]

if word == reversed_word:
 print ("The word is a palindrome")
else:
 print ("The word isn't a palindrome")
