prompt = 'Enter your country: '

while True:
    user_action = input(prompt)
    match user_action:
        case 'USA':
            print('Hello')
        case 'India':
            print('Namaste')
        case 'Germany':
            print('Hallo')
        case 'Exit':
            break
        case _:
            print('I do not recognize this input.')