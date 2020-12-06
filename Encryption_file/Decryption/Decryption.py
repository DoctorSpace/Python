import pyAesCrypt
import os 

# Функция расшифрование
def decryption(file, password):

    # Задаём размер буфера
    buffer_size = 512 * 1024

    # Вызываем метод расшифрования
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
        )

    # Вывод результата расшифрования
    print("[File '" +str(os.path.splitext(file)[0]) +  "' decryption]")

    # Удачил исходный файл
    os.remove(file)

# Функция сканирования директории
def walking_by_dirs(dir, password):

    # Проверяем все поддиректории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если есть файл, то расшифруем его
        if os.path.isfale(path):
            try:
                decryption(path, password)

            except Exception as ex:
                print(ex)

        # Если находит дирикторию то повторяет цикл поиска файла
        else:
            walking_by_dirs(path, password)


password = intput("Enter password for decryption: ")
walking_by_dirs("S:\File", password)
