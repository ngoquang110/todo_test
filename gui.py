import functions
import FreeSimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What do u want to do?")],
          [sg.Input(tooltip='Enter todo',key='todo'),sg.Button('Add')],
          [sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45,10]),sg.Button('Edit')],
          [sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout, font = ('Helvetica',20))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    print(event)
    print(values)
    # See if user wants to quit or window was close
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
        case 'Edit':
            todo = values['todos'][0]

            todos = functions.get_todos()
            index = todos.index(todo)
            todos[index] = values['todo'] + '\n'

            functions.write_todos(todos)
            #Update
            window['todos'].update(values = todos)
        case 'todos':
            window['todo'].update(value = values['todos'][0])
        case sg.WINDOW_CLOSED:
            break
        case 'Quit':
            break

# Finish up by removing from the screen
window.close()