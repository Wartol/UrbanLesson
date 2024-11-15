import os
import time

for root, dirs, files in os.walk('.'):
  for file in files:
    filepath = os.getcwd()
    filetime = os.path.getatime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')