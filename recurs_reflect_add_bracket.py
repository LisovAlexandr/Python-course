'''
Описание модуля
'''
def rec_reflection(st:str, lst:list = None) -> str:
    """takes a string 'as(d(((f' and return string + recurse reflection 'as(d(((ff)))d)sa'
    'as(d((f' -> 'as(d((ff))d)sa'  when len str even
    'as(d((f' -> 'as(d((ff))d)sa'  when len str odd
    :param st:   string for change
    :param lst:  list for result
    :return:     result string"""
    if lst == None:
        # к нашей строке s будем дописывать развернутую s
        # теперь в функции появился lst для созранения результата

        lst = list(st)
    if len(st) == 0:
        # здесь решение рекурсии, как бы конец цикла, когда срез строки достигнет нуля
        return ''.join(lst)  # здесь решение рекурсии, как бы конец цикла
    if st[-1] == '(':
        # в s заменяем '(' на ')'

        lst.append(')')
    else:
        # добавляем последний элемент st в конец lst

        lst.append(st[-1])
    # не забываем добавить второй параметр lst, где хранится результат
    return rec_reflection(st[:-1], lst)

def rec_add_bracket(st):
    # рекурсивно добавляет скобки в строку -> с(т(ро)к)у
    '''takes a string 'asdf' and return string with bracket 'a(A(B)C)f'
    'aABCf' -> 'a(A(B)C)f'  when len str even
    'aABCfa' -> 'a(A(BC)f)a'  when len str odd
    :param st:
    :return:
    '''

    if len(st)==2 or len(st)==1:
        return st
    return st[0] + "(" +  rec_add_bracket(st[1:-1])   + ")" + st[-1]

# # # TEST # # #
s= 'aABCf'
print(rec_add_bracket(s))
print(rec_reflection(s))
# print(s)                # A(B(C
# print(rec(s))           # A(B(CC)B)A
# print(rec.__annotations__)