""" sort метод списка, sorted() встроенная функция языка python"""
a = [1, 4, 6, 43, 6, -7]

# метод sort изменяет список
a.sort()
print(a) # [-7, 1, 4, 6, 6, 43]

## a = a.sort() ## если присвоить, то получим a = None

# функция sorted() не изменяет начальную коллекцию
a = sorted(a)

# sort и sorted принимают два параметра
a = sorted(a,key=function, reverse=True)
a.sort(key=function, reverse=True)