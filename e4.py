import webbrowser

user_term = input('Search something here: ')

webbrowser.open(f'https://www.google.com/search?q={user_term}')