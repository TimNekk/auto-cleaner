import pickle
import os
import shutil
import time

path = r'C:\Users\Tim PC\AppData\Local\Temp'
files_deleted = 0

files_amount = len(os.listdir(path))
print('Очистка ' + str(files_amount) + ' файлов в дериктории:\n' + path)

if os.path.isdir(path):
    files = os.listdir(path)
    for file in files:
        try:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                files_deleted += 1
            else:
                shutil.rmtree(file_path)
        except PermissionError:
            pass

print('\nУдаленно          ' + str(files_deleted) + ' файлов\nПроигнорированно  ' + str(files_amount - files_deleted) + ' файлов')
