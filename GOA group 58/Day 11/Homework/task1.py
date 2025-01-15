# 1) გააიაზრეთ ეს კოდი, დაკომენტარეთ თითოეული კოდი

# Set the password that the user will have to enter.
secret_pass = "luka1234"
# Initialize a variable to store the password entered by the user.
user_pass = ''
# Set the number of attempts to enter the password, starting with 3.
tries = 3
# Start a loop that will run until the number of attempts is greater than 0 and the password does not match the secret one.
while tries > 0 and user_pass != secret_pass:
    # Ask the user to enter the password and specify the remaining number of attempts.
    user_pass = input("Enter your password (you have " + str(tries) + " tries left): ")
    # Decrease the number of attempts by 1 after each attempt.
    tries = tries - 1
# Check if the entered password matches the secret one.
    if user_pass == secret_pass:
        # If the passwords match, display a message about successful access
        print("Access granted!")
        # If the passwords do not match and attempts have ended:
    elif tries == 0:
        # Notify the user that he has reached the maximum number of attempts and access is denied.
        print("You've reached the maximum number of tries. Access denied!")
        # If the passwords do not match and attempts are still remaining:
    else:
        # Notify that access is denied and offer to try again.
        print("Access denied! Try again.")