
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    if 'show' in user_action:
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            listItem = f"{index + 1}. {item.capitalize()}"
            print(listItem)

    if 'edit' in user_action:
        number = int(input('Number of the todo to edit: '))
        number = number - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        print('Here is todos existig: ', todos)

        new_todo = input('Enter replacement for to do: ')
        todos[number] = new_todo + '\n'
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        print('Edited succesfully! Here is the new list: ', todos)
        

    if 'complete' in user_action:
        number = int(input('Number of the todo to complete: '))
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(number-1)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo '{todo_to_remove}' was removed from the list."
        print(message)

    if 'exit' in user_action:
        break

print('Bye!')