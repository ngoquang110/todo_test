import shutil

# Kiểm tra dung lượng ổ đĩa
usage = shutil.disk_usage('/')
print(f'Total: {usage.total}, Used: {usage.used}, Free: {usage.free}')

# Tìm kiếm đường dẫn đến file thực thi
path_to_python = shutil.which('python')
print(f'Path to Python: {path_to_python}')

#Tạo file nén
shutil.make_archive('output','zip','Files')