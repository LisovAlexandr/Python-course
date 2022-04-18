""" использовании функции isinstance для работы с элементами разного типа в одном списке"""
# конкатенация строк из списка a
s_strock = ''
a = [1, 4, 'hello' ,8 ,' world' ,5 ,6, [1, 2], [5], 10.0]
for i in a:
    if isinstance(i,str):
        s_strock = s_strock + i
print(s_strock)
# сложение цифр из списка a
s_digit = 0
for i in a:
    if isinstance(i,(int,float)):
        s_digit += i
print(s_digit)
# сложение списков
s_list = []
for i in a:
    if isinstance(i,list):
        s_list = s_list + i
print(s_list)

