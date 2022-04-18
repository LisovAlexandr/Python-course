"""работа с функцией filter()"""

a='asdfadsKGHKJGH1234879'
# вернем цифры из строки 'a' c помощью метода строки, пишется без скобок
digit = list(filter(str.isdigit,a))
print(digit)
# вернем буквы
alpha = list(filter(str.isalpha,a))
print(alpha)
# вернем заглавные буквы
upper = list(filter(str.isupper,a))
print(upper)

# # использование собственной фукнции
# найдем четные в списке
def f(x):
    return x%2 == 0
num = [1, 3, 54, 56, 3, 2, 656, 121]
even = list(filter(f, num))
print(even)
# найдем больше 20 в списке
def f(x):
    return x>10
num = [1, 3, 54, 56, 3, 2, 656]
more10 = list(filter(f, num))
print(more10)

# # встроенные функции
# убрать нули
num2 = [1, 3, 0, 0, 54, 56, 0, 3, 2, 656, 0]
null = list(filter(bool,num2))
print(null)
    ## либо так ##
null2 = list(filter(None,num2))
print(null2)

# # филтрация словарей

# вернем список городов, где значение больше 500
d = {
    'Moscow': 700,
    'New-York': 8000,
    'London': 100
}
more500 = list(filter(lambda x: d[x]>500,d))
print(more500)
