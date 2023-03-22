pass_prompt = "Enter a password: "
pass_error = 'Your entered password is incorrect, please, try again!'
password_in = input(pass_prompt)

while password_in != "pass123":
    print(pass_error)
    password = input(pass_prompt)

print("Password was correct!")