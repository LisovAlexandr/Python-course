"""функция filter вернет строки из четырех букв или строки начинающиеся с S, отсортированный по алфавиту"""

days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
four_char = list(filter(lambda x: (len(x)==4 or x[0] == 'S'),days))
four_char = sorted(four_char,reverse=True)
# вывод каждого значения списка на новой строке генератором
[print(i) for i in four_char]