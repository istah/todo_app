while True:
    prompt = "Please enter a title of book (or 'quit' to exit): "
    title = input(prompt)
    if title == 'quit':
        break
    print("The length of the title is " + str(len(title)) + " characters.")