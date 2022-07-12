echo off
title Create exe
pyinstaller --onefile --icon="C:\Users\Doctor Space\YandexDisk\code\Python\Steam_Game\Game.ico" "C:\Users\Doctor Space\YandexDisk\code\Python\Steam_Game\Steam_Game.py"

or
echo off
pyinstaller -F -i "C:\Users\Doctor Space\YandexDisk\code\Python\Steam_Game\Game.ico" Steam_Game.py

