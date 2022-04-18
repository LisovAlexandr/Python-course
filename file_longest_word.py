'''The module finds the longest word in the file, ignoring punctuation marks, number of three-digit numbers, number of three-digit numbers,sum of two-digit numbers'''


def remove_punctuation(st):
    '''
    remove all punctuations from string
    :param st:
    :return: changed string
    '''
    from string import punctuation
    for sign in st:
        for sign in punctuation:
            st = st.replace(sign, '')
    return st


def longest_word_in_file(file_name):
    '''
    return the longest word in string ignoring punctuation marks
    :param file_name:
    :return:
    '''
    file = open(file_name, 'r', encoding='utf-8')
    length = 0
    longest_word = ''
    num3 = []
    num2 = []

    for line in file:
        for word in line.split():

            # удалим из word все символы, вызвав функцию
            word = remove_punctuation(word)

            if length <= len(word):
                length = len(word)
                longest_word = word

            # найдем все трехзначные числа(задание)
            if len(word) == 3:
                num3.append(int(word))
            # найдем все двухзначные числа(задание)
            if len(word) == 2:
                num2.append(int(word))

    # вернем самое длинное слово
    # задание: количество трехсимвольных слов, сумма двухзначных чисел
    return longest_word,len(num3),sum(num2)


print(longest_word_in_file('numbers.txt'))
