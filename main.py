# # sсript = input('Введите команду')
# s='''SET GCELLVAMOS: IDTYPE=BYID, CELLID=0, VamosSwitch=VHR, VamosAssSwitch=ON, VamosMultLoadThd=75, VamosIntraHoSwitch=ON, VamosMainTsc=0,
# VamosSubTsc=2, VamosLoadReuseSwitch=ON, VamosLoadReuseLoadThd=25, VamosQualReuseSwitch=ON, MuteSaicSwitch=ON, MuteSaicIdeSwitch=OFF,
# SaicProMsSwitch=ON, SaicProMsIdeSwitch=OFF, UnkownSaicMultSwitch=ON, MultAllowBeforeConn=OFF, SaicWhtMsIdentSw=OFF;'''
# print(s[:4]+s[5:].replace(', ','\n'))
'''
stri=list('{[]}()')
print(stri)
i=0
#print(stri[i])
n=len(stri)
while i<n:
    print('начало цикла ', stri)
    if n==1:
        break
    if stri[i]=='(' and stri[i+1]==')' or stri[i]=='[' and stri[i+1]==']' or stri[i]=='{' and stri[i+1]=='}':
        stri.remove(stri[i])
        stri.remove(stri[i])
        n=len(stri)
        print(stri)
        i=0
    else:
        i+=1
        #input('блок else')
if n!=0:
    print('NO')
else:
    print('YES')
'''
# import shlex

'''
my_list = list(dict.fromkeys([4, 7, 5, 5, 4, 7, 'qwer', 'dfgdfg', 'qwer']))
print(my_list)
print(list(dict.fromkeys(my_list)))
'''
# my_list2=[]
# [my_list2.append(i) for i in my_list if i not in my_list2]

# st='ZZzzzZ34 WWw777'.lower()
# print(st)
# d={}
# for i in st:
#     if i.isalpha():
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
# print(d)
'''
a={1,3,5,2}
print([i for i in sorted(a)])
'''
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
# list=sorted(subject_marks, key= lambda x: int(x[1]))
# for i in list:
#     print(i[0],i[1],type(i))
'''
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
list=sorted(subject_marks, key= lambda x: x[1],reverse=True)
for i in list:
    print(i[0],i[1])
'''
'''
subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# subject_marks=sorted(subject_marks,key=lambda x: x[0])
list=sorted(subject_marks,key=lambda x: (-x[1],x[0]))

for i in list:
    print(i[0],i[1])
'''
# a = list('asddfghh')
# b = set(a)
# for i in a:
#     if i in b:
#         print(i, end='')
#         b.remove(i)
# sorted(a,reverse=)
'''
dict={'Били': ['aaaa', 'aaa'], 'Вили': [], 'Дили': ['aaaa', 'aaaa', 'aaaa']}
for i in dict:
    dict[i]=len(set(dict[i]))
dict=sorted(dict.items(),key=lambda x:-x[1])
for i in dict:
    print(f'Количество уникальных комментаторов у {i[0]} - {i[1]}')
'''
# print(set('1235'))
# n=1900
# for i in range(n+1,9000):
#     #print(set(str(i)))
#     if len(set(str(i)))==4:
#         print(i)
#         break
'''
input='{a, b, c, c}'
str=[i for i in input if i.isalpha()]
print(len(set([i for i in input() if i.isalpha()])))
'''

# myList=[1, 1, 1, 1, 1, 2, 2, 2, 2, 3]
# dubl={}
# for item in myList :
#     count = 0
#     for x in myList :
#         if x == item :
#             count += 1
#     dubl[item]=count
# print(dubl)
# listdub=[]
# for i in dubl:
#     if dubl[i]>1:
#         listdub.append(i)
# print(listdub)

'''
def format_namelist(list_dicts):
    names = []
    for i in list_dicts:
        names.append(i['name'])
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return (names[0] + ' и ' + names[1])
    if len(names) > 2:
        return (", ".join(names[:-2]) + ', ' + names[-2] + ' и ' + names[-1])


list_dicts = [{'name': 'Bart'}, {'name': 'Lisa'}]  # , {'name': 'Maggie'}]
print(format_namelist(list_dicts))
'''
# domain_name("http://google.com") # возвращает "google"
# domain_name("http://google.co.jp") # возвращает  "google"
# domain_name("www.xakep.ru") # возвращает "xakep"
# domain_name("https://youtube.com") # возвращает "youtube"
# domain_name("https://www.asos.com") # возвращает "asos"
# domain_name("http://www.lenovo.com") # возвращает "lenovo"
'''
str='domain_name("http://google.com")'

str=str.lstrip('domain_name("').rstrip('")')
print(str)
if 'http://' in str:
    str=str.replace('http://','')
if 'https://' in str:
    str=str.replace('https://','')
if 'www.' in str:
    str=str.replace('www.','')
str=str.split('.')[0]
print(str)
'''
# def func(ls):
#
#     if len(ls) == 0:
#         return
#     if len(ls)>0:
#         print(ls[-1], end = " ")
#         ls=ls[:-1]
#     return func(ls)
#
# s=[1, 2, 3]
# st=list(input().split())
# print(st)
# func(s)
# print(st[:-1])
# print(st[1])
# while len(st)>=1:
#     print(st)
#     st=st[1:-1]
"""
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=7
print(fib(n))
"""
#
# sum=0
# def list_sum_recursive(ls):
#     if len(ls)>=1:
#         print('')
#         return list_sum_recursive(ls[:-1])
#     return sum
#
# ls=[1, 2, 3]
# print(ls[:-1])
# # print(list_sum_recursive(ls))


# import recurs_reflection_str
# s='a(d(g'
# print(recurs_reflection_str.rec(s))
# help(recurs_reflection_str)
# import annotation
# help(annotation)