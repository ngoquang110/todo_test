FILE_PATH = 'text.txt'
def get_todos(filepath = FILE_PATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath = FILE_PATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# Nếu mà không có cái này thì dòng này sẽ luôn luôn hiển thị
if __name__ == '__main__':
    print("Hello")