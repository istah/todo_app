
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                listItem = f"{index + 1}. {item.capitalize()}"
                print(listItem)

        case 'edit':
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
            

        case 'complete':
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

        case 'exit':
            break

        case _:
            print('I do not recognize this input.')

print('Bye!')