from functions import get_todos,write_todos
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is ', now)

todos = []

while True:
    user_action = input('Enter method(add,show,exit): ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        if len(user_action) > 3:
            todos.append(todo)
            with open('text.txt', 'a') as file:
                file.write(todo)
        else:
            print('error')

    elif user_action.startswith('show'):

        todos = get_todos()

        new_todos = [x.strip('\n') for x in todos]

        for index,x in enumerate(new_todos):
            print(f'{index+1}. {x}')

    elif user_action.startswith('edit'):
        try:
            index = int(user_action[5:])
            index -= 1

            new_todo = input('Enter your update: ') + '\n'
            todos[index] = new_todo

            write_todos(todos)

        except ValueError:
            print('Error! Reboot')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            index = number - 1

            #Take from file
            todos = get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            #Write to file
            write_todos(todos)

            print(f'Todo {todo_to_remove} was removed from todos')
        except IndexError:
            print('Error! Input smaller numbers')
            continue

    elif user_action.startswith('exit'):
        break

    elif user_action.startswith('clear'):
        todos.clear()
        # Clear and rewrite to file
        write_todos(todos)

    else:
        print('Error!')

