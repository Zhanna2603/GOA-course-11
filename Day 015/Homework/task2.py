"""Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords."""

count = 0 
correct_password = "Goa best"
while True:
    password = input("Enter the password:")
    if password == correct_password:
        print("Entered password is correct")
        break
    else:
        count += 1
        print("Entered password is incorrect")
print(f"Entered of incorrect passwords: {count}")