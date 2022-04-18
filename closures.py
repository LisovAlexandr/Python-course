
def average_numbers():
    '''
    подсчет среднеарифметического с помощью замыканий
    :return:
    '''
    numbers=[]
    count=0
    def inner(a):
        nonlocal numbers  #тут говорим, что будет изменяться внешний список numbers, чтобы хранить данные после завершения функции inner
        nonlocal count
        numbers.append(a)
        count+=1
        print(f'Функция вызывалась {count} раз')
        print(numbers,end=' ')  #тут будем выводить то, что накопилось в списке numbers
        return sum(numbers)/len(numbers)
    return inner
aver=average_numbers()
# присвоили результат average_ переменной aver. Теперь aver хранит функцию inner со счетчиком count и списком numbers, которые сейчас обнулились при первом вызове average_numbers
# print(aver(10)) # вызываем функцию inner с очередным значением переменной a
# print(aver(20))
# print(aver(30))

# from datetime import datetime
from time import perf_counter
# print(perf_counter())
def timer():
    """
    функция считает, сколько времени прошло между вызовом timer и вызовом t(), в которой inner
    :return:
    """
    start = perf_counter()   # тут инциируется и запоминается время вызова timer
    def inner():
        #nonlocal start
        return perf_counter() - start
    return inner
t = timer()  # тут в t фактически будет inner
# print(t())   # в этот момент вычисляется прошедшее время
# print(t())   # тут уже следующее время

## подсчет количества вызовов функции add

def add(a,b):
    return a+b

def call_counter(func):
    """функция подсчитывает сколько раз будет вызываться другая заданная функция"""
    count=0
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        print(f'Функция {func.__name__} вызывается {count} раз')
        return func(*args,**kwargs)
    return inner

call= call_counter(add)  # тут как бы замкнули функцию add и теперерь в переменной call будет производиться подсчет каждого вызова
print(call(2,3))
print(call(15,5))
print(call(4,6))