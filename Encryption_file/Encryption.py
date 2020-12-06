import pyAesCrypt
import os 

# Функция шифрования
def encryption(file, password):

    # Задаём размер буфера
    buffer_size = 512 * 1024

    # Вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file)+ ".crp",
        password,
        buffer_size
        )

    # Вывод результата шифрования
    print("[File '" +str(os.path.splitext(file)[0]) +  "' encryption]")

    # Удачил исходный файл
    os.remove(file)

# Функция сканирования директории
def walking_by_dirs(dir, password):

    # Проверяем все поддиректории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если есть файл, то шифруем его
        if os.path.isfale(path):
            try:
                encryption(path, password)

            except Exception as ex:
                print(ex)

        # Если находит дирикторию то повторяет цикл поиска файла
        else:
            walking_by_dirs(path, password)


password = input("Enter password for encryption: ")
walking_by_dirs("S:\File", password) #Необходимо указать место файлов