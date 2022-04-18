# нахождение суммы всех делителей
'''
n = 34
i = 1
sum = 0
while i < n:
    if n % i == 0:
        print(i, end=' ')
        sum += i
    i += 1
print(sum + n)
'''
'''
a, b = 75, 120
c=a
d=b
while a!=b:
    if a>b:
        a=a-b
    if b>a:
        b=b-a

print(c*d/a)
'''
'''
#l=list(map(int,list(input())))
l=[0,2,2,1,2]
count=[0]*len(l)
#print(count[1], l[3])
print(type(l[0]))
for i in l:
    print(count[i])
print(count)
'''
# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17,18]]
# gen=[vector[i][j] for i in range(len(vector)) for j in range(3)]
# print(gen)
'''
data = {
    'my_friends':
        {'count': 10,
         'items': [
             {'first_name': 'Kurt',
              'id': 621547005,
              'last_name': 'Cobain',
              'bdate': '31.8.2005'},
             {'first_name': 'Виолетта',
              'id': 484200150,
              'last_name': 'Кастилио'},
             {'first_name': 'Иринка',
              'id': 21886133,
              'last_name': 'Бушуева',
              'bdate': '28.8.1942'},
             {'first_name': 'Данил',
              'id': 282456573,
              'last_name': 'Греков',
              'bdate': '4.7.2002'},
             {'first_name': 'Валентин', 'id': 184902932, 'last_name': 'Долматов', 'bdate': '25.5'}, {'first_name': 'Евгений', 'id': 620469646, 'last_name': 'Шапорин', 'bdate': '6.12.1982'}, {'first_name': 'Ангелина', 'id': 622328862, 'last_name': 'Краснова', 'bdate': '4.11.1995'}, {'first_name': 'Иван', 'id': 576015198, 'last_name': 'Вирин', 'bdate': '2.2.1915'}, {'first_name': 'Паша', 'id': 386922406, 'last_name': 'Воронов', 'bdate': '27.9'}, {'first_name': 'Ольга', 'id': 622170942, 'last_name': 'Савченкова', 'bdate': '20.12'}]}}
# print(i.get('first_name') for i in data.get('my_friends').get('items'))
list=[]
for i in data.get('my_friends').get('items'):
    # print(i.get('first_name'))
    list.append(i.get('first_name'))
# list = sorted(list)
for i in list:
    print(i)
# print(*sorted(i for i in list),sep='\n')

# print(*sorted([i['first_name'] for i in data['my_friends']['items']]), sep='\n')
'''
'''
st = ['asdf']
st2 = ['fdsaq']
if sorted(st) == sorted(st2):
    print('ok')
else:
    print('not ok')
print(st[::-1])
'''
'''
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
# print(morze)
for i in input().lower().split():
    for j in i:
        print(morze[j], end=' ')
    print()
'''
'''
people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]
phone_book = {i[1]: i[0] for i in people}
print(phone_book)
'''
'''
a=(1,2,3)
sum=0
for i in a:
    sum+=i
print(sum/len(a))
print(a)
'''
'''
models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]
for i in sorted(models, key=lambda x: x['color']):
    print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}")
'''
# Sony PlayStation 5: 46000
# Телевизор QLED Samsung QE65Q60TAU: 87090
# Смартфон Samsung Galaxy A11: 10000
# Планшет Samsung Galaxy Tab S6: 26600
# конец
# a = 'Sony PlayStation 5: 46000'
# list = []
# # while input() != 'конец':
# list.append(a.split(sep=':'))
# print(list)
'''
list = [['Sony PlayStation 5', '46000'],
        ['Телевизор QLED Samsung QE65Q60TAU', '87090'],
        ['Смартфон Samsung Galaxy A11', '10000'],
        ['Планшет Samsung Galaxy Tab S6', '26600']]
for i in sorted(list, key=lambda x: -int(x[1])):
    print(i[0],i[1])
'''
# dict = {'Леонардо Ди Каприо': 3, 'Джонни Депп': 2, 'Мэтт Деймон': 1}
# fin = [i for i in sorted(dict.items(), key=lambda x: -x[1])]
# print(*fin[0],sep=', ')
# print(*fin[-1],sep=', ')
# if isdigit()
'''
import  turtle
turtle.speed(1)
turtle.forward(100)
'''
# st = 'domain_name("https://youtube.com")'.replace('domain_name("', '').replace('")','')
# if 'http://' in st:
#     st=st.replace('http://','')
# if 'https://' in st:
#     st=st.replace('http://','')
# if 'www.' in st:
#     st=st.replace('www.','')
# st=st.split('.')[0]
# print(st)
'''
st = 'https://youtube.com'
st1 = 'http://google.co.jp'
st = st.strip('https://http://.com.co.jp')
print(st)
'''
# sum = 1
# for i in range(1, 31):
#     sum *= i
# c=0
# print(sum,type(sum))
# # print(sum,str(sum).count('0'))
# while sum%10==0:
#     sum=sum//10
#     c+=1
# print(c)
"""
def summir(a,b):
    '''
    description function
    :param a:
    :param b:
    :return:
    '''
    return a+b
help(summir)
"""

# def print_goods(*args):
#     num = 1
#     for i in args:
#         if type(i) is str and i != '':
#             print(f'{num}. {i}')
#             num += 1
#     if num == 1:
#         print('Нет товаров')
#
#
# print_goods(1, True, 'Грушечка', '', 'Pineapple')
"""
def info_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(k, v)


info_kwargs(first_name="John", last_name="Doe", age=33)
"""

# def list_sum_recursive(ls, su):
#     if len(ls) == 0:
#         return su
#     su = su + ls[0]
#     return list_sum_recursive(ls[1:], su)
#
#
# sum1 = 0
# ls1 = '1 2 3'
# ls2 = [int(i) for i in ls1.split()]
# print(ls2)

# print(list_sum_recursive(ls1, sum1))
'''
def list_sum_recursive(ls):
    if len(ls) == 1:
        return int(*ls)
    ls[0] = ls[0] + ls[-1]
    return list_sum_recursive(ls[:-1])


ls1 = [1, 2, 3, 4]
print(list_sum_recursive(ls1))
'''

a = []


def flatten(lst, my_list=None):
    if my_list == None:
        my_list = []
    for i in lst:
        if type(i) == int:
            my_list.append(i)
        else:
            flatten(i, my_list)
    return my_list


l = [1, [2, 3], [[2], 5], 6]
print(flatten(l))
