"""4)Write a program that simulates a basic ATM. It should ask the user for their PIN, and if it's correct, display a text withdrawal, deposit, and balance."""

pin_code = "1234"
user_pin = input("Enter PIN: ")

if user_pin == pin_code:
    print("1.Cash out money \n 2.Deposit money \n 3.Check balance")
else:
    print("PIN is incorrect")