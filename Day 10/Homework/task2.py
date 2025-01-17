"""2) ამ ფოტოს მიხედვიტ გააკეთეთ პროგრამა. (მოხმარებელს შემოატანინეთ პაროლი იქამდე სანამ არ დაემტხვევა რეგისტრირებულ პაროლს, while ციკლის და  if else _ის გამოყენებით)"""

password = 153870

while True:
    user_password = int(input("Enter password: "))
    if user_password == password:
        print("True!")
        break
    else:
        print("Failed!")