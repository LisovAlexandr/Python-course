"""all и any аналог булевых && и ||"""

a = ['asdf','dfg','fgh','dfg']
print(all(a))  # True когда все элементы True, аналог И
a2 = ['asdf','dfg','fgh','dfg','']
print(all(a2))  # False

b = ['asdf','dfg','fgh','dfg']
print(any(b))  # True когда хотя бы один элемент True, аналог ИЛИ
b2 = ['asdf','dfg','fgh','dfg','']
print(any(b2))  # все еще True
b3 =['','','','']
print(any(b3))  # False так как все элементы ложны