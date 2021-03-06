""" zip соединяет два или более списком по одинаковым индексам с результатом минимального списка"""
a = [1,4,7,5]
b = [667,4567,656,909]
rez = list(zip(a, b))
# возвращает список кортежей с элементами списка a b на одинаковых индексах
print(rez)

a = [1,4]
b = [667,4567,656,909]
# zip сцепит по наименььшему списку, лишние значения опустит
rez = zip(a, b)
print(rez) # zip итератор

# итератор можем опойти только один раз
for i in rez:
    print(i)

# тут ничего не выведется
for i in rez:
    print(i)

# соединим три списка
a = [1,4,7,5]
b = [667,4567,656,909, 5345]
c = 'asdf'

rez3 = list(zip(a,b,c))
print(rez3) # -> [(1, 667, 'a'), (4, 4567, 's'), (7, 656, 'd'), (5, 909, 'f')]
for i in zip(a,b,c):
    print(i)

# получим списки обратно из zip, множественное присвоение

col1,col2,col3 = zip(*rez3)
print(col1,col2,col3)
