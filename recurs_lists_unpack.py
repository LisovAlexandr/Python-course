def list_unpack(lst, level=1):
    """
    takes list of lists and print inserted list, show nesting level
    :param lst:
    :param level:
    :return:
    """
    #рекурсия будет работать с вложенными списками либого уровня, чего не сможет for
    print(level, 'level:',*lst)
    for i in lst:
        if type(i) == list:
            list_unpack(i,level+1)

l = [1, 2, [2, 3], 4, [3, 4, [2, 3], 5]]

list_unpack(l)
