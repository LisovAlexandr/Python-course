import os

path = 'C:\\test'

def obhodfile(path, level=1):
    print('Level = ', level, 'Content: ',os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся в', path +'\\'+i)
            obhodfile(path +'\\'+i,level+1)
            print('Возвращаемся в',path)

obhodfile(path)