import os


def recurs_folder(folders, dict1=None):
    if dict1 == None:
        dict1 = {'files': [], 'folders': []}
    for i in os.listdir(folders):
        print('смотрим папку ', i, end=' ---> ')
        if os.path.isdir(folders + '\\' + i):
            print(i, ' это папка. Открываем ', folders + '\\' + i)

            recurs_folder(folders + '\\' + i, dict1)
            print('Больше ничего нет. Идем в папку выше')
        else:
            print('вообще то это файл. Идем дальше по списку...')
            dict1['files'].append(i)
    return dict1


path1 = 'C:\\test'

dict=recurs_folder(path1)
print(dict['files'])

# filestat = os.stat('C:\\test\\infofile.txt')
# print(filestat)
# dict1 = {'files': 0, 'folders': 0}
# dict1['files']+=1
# print(dict1)
