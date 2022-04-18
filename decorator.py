def decorator(func):

    def inner():
        print('start decorator...')
        func()
        print('finish decorator...')
    return inner

def say():
    print('hello!')

h=decorator(say)  # тут просто работает замыкание
# h()   # вызвали inner
##  далее произойдет расширение функционала say с помощью декоратора
say=decorator(say)  # используем то же имя что и назвыние функции для модернизации
# say()   # важно помнить что в say теперь хранится ссылка не на original say, а на функцию inner

# # теперь сделаем новую функцию
def bye():
    print('bye-bye!')
bye=decorator(bye)
# bye()

## случай когда нам нужны аргументы в декорируемой функции
def decorator2(func):
    """
    в этот декоратор можем запихивать функцию с любым количество аргументов, и даже без них.
    С помощью *args,**kwargs всве аргументы обработаются в соотвтетствии с декорируемой функцией
    :param func:   функция для декорации
    :return:  inner функция-замыкание
    """

    # принять за правило *args,**kwargs
    def inner(*args,**kwargs):  # аргументы ЛУЧШЕ указывать *args,**kwargs, чтобы не получать ошибку, когда неправильное кол-во аргументов
        print('start decorator...')
        func(*args,**kwargs)    # проброс аргументов через замыкание
        print('finish decorator...')
    return inner

def hi_name(name):
    print('Hi, ', name)

# это еще не декорирование функции, но объясняет принцип
hi_name = decorator2(hi_name)
# hi_name("Vasya","Vasya2")    # тут будет ошибка: декоратор пробросит все аргументы в original функцию, но original функция принимает только один аргумент

# сейчас будет декорирование функции, "навешивание" декоратора

def header(func):
    def inner(*args,**kwargs):
        print('<h1>')
        func(*args,**kwargs)
        print('</h1>')
    return inner
def table(func):
    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')
    return inner


'''такой способ декорирования используется в разработке'''
@header     # эта строчка делает то же самое, что и html=header(html)
@table      # эта строчка делает то же самое, что и html=heade(table(html))
# первым сработает декоратор table, а уже за ним header
def html():
    print('здесь когда-то будет html код')

# html=header(html)
html()

'''как не потерять имя функции и doc при декорировании'''
# способ 1

def decor__name__(func):
    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')
    inner.__name__ = func.__name__ # подменяем имя inner на имя func, которую декорируем
    inner.__name__ = func.__name__
    return inner

# способ 2   декоратор wraps

from functools import wraps

def decor_wraps(func):
    @wraps(func)   # тут происходит декорация inner с помощью wraps, а аргументом будет наша функция func
    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')

    return inner