prompt = input("Enter a new password: ")
if len(prompt) > 7:
    print("Great password there!")
elif len(prompt) == 7:
    print("Password is Ok, but not too strong.")
else:
    print("Your password is weak.")

