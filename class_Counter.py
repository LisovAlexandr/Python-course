"""модуль collections"""

from collections import Counter

b = 'asdff'
# класс Counter подсчитает колво символов в строке или списке и выведет в виде словаря
d = Counter(b)
print(d) # Counter({'f': 2, 'a': 1, 's': 1, 'd': 1})
