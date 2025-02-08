# Завдання 1

# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, 
# переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.

# Також візьміть до уваги наступні умови:
# 1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка:
# шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

# 2. Рекурсивне читання директорій:
# Має бути написана функція, яка приймає шлях до директорії як аргумент.
# Функція має перебирати всі елементи у директорії.
# Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він має бути доступним для копіювання.

# 3. Копіювання файлів:
# Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
# Файл з відповідним типом має бути скопійований у відповідну піддиректорію.


import os
import shutil
import sys

def sort_files(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
        
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        if os.path.isdir(src_path):
            sort_files(src_path, dest)
        else:
            file_ext = item.split('.')[-1]
            ext_dir = os.path.join(dest, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.copy(src_path, ext_dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [destination_directory]")
        sys.exit(1)
        
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"

    sort_files(source_directory, destination_directory)