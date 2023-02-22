import os
import shutil
import pathlib
from pathlib import Path
import Image
from PIL import Image


# Путь к исходной директории
dir_path = pathlib.Path.cwd()

# Исходный
source_folder = rf'{dir_path}\Image\\'
# Назначение
destination_folder = rf'{dir_path}\Directory\\'
destination_thumbnails_folder = rf'{dir_path}\Directory\thumbnails\\'

size = 200, 112

# Изменить размер всех файлов
for file_name in os.listdir(source_folder):
    source = source_folder + file_name
    img = Image.open(source)
    new_image = img.resize((200, 112))
    new_image.save(destination_thumbnails_folder + file_name)


# Копировать файлы из Исходного в Назначение
for file_name in os.listdir(source_folder):
    # построить полный путь к файлу
    source = source_folder + file_name
    destination = destination_folder + file_name
    # копировать только файлы
    if os.path.isfile(source):
        shutil.copy(source, destination)

print('Копирование завершино')