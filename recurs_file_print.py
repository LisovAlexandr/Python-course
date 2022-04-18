"""рекурсивный обход папок и файлов в них"""
import os


def recurs_folder(folders):
    for i in os.listdir(folders):
        print('смотрим папку ', i, end=' ---> ')
        if os.path.isdir(folders + '\\' + i):
            print(i, ' это папка. Открываем ', folders + '\\' + i)
            recurs_folder(folders + '\\' + i)
            print('Больше ничего нет. Идем в папку выше')
        else:
            print('вообще то это файл. Идем дальше по списку... ')


path1 = 'C:\\test'
print(os.path.isdir(path1))
recurs_folder(path1)
# print(os.listdir(path1))
# filestat = os.stat('C:\\test\\infofile.txt')
# print(filestat)
