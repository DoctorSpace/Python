import os
import shutil
import pathlib
from pathlib import Path
import Image
from PIL import Image



# destination - путь к папке со скриншотами
print('Введите путь куда загружать фотографии (screenshots): ')
#destination_path = input()
destination_path = r'C:\Programs\Launchers\Steam\userdata\163259359\760\remote\15196443846402637824\screenshots\\'

#destination_path = input()
print('Добавить название картинки от которой вставлять фотки (пример: 20230223012126_1.jpg): ')
#image_stop = input()
image_stop =  r'20230225164529_1.jpg'

############ 

# Путь к исходной директории
dir_path = pathlib.Path.cwd()

# Новые_входящие
source_folder = rf'{dir_path}\Image\\'


# Назначение (добавить \\ вконце)
destination_folder = rf'{destination_path}'
destination_thumbnails_folder = rf'{destination_path}\thumbnails\\'


arr_img = []
test = 0

# запись в массив список вторичных фотографий
for file_name in os.listdir(destination_path):
    if file_name == image_stop or test > 0:
        source = destination_path + file_name
        test = test + 1
        # Проверка только на картинки
        if os.path.isfile(source):
            arr_img.append(file_name)

# Проверка на количество фотографий 
count_good_photo = 0
for file_name in os.listdir(source_folder):
    source = source_folder + file_name
    if os.path.isfile(source):
        count_good_photo = count_good_photo + 1
if len(arr_img) <= count_good_photo:
    print('Список маленький, сделайте ещё фотографий вторичной игры')

count_arr = 0
# Переименовка файлов
for file_name in os.listdir(source_folder):
    source = source_folder + file_name
    new_sourse = source_folder + arr_img[count_arr]
    count_arr = count_arr + 1
    os.rename(source, new_sourse)



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