"""Write a program that asks the user to enter a password. If the password is "abc123", print "Access granted"; otherwise, print "Access denied"."""

password = input("Enter password:")
if password == "abc123":
    print("Access granted")
else:
    print("Access denied")