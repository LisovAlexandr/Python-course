""" задача про домашнюю и выездную форму футболистов"""
lst = ['100 42', '42 100', '5 42', '100 5']
counter = 0
lst = [i.split() for i in lst]
print(len(lst))
for i in range(len(lst)):
    print(lst[i])
    print()
    for j in range(len(lst)):
        if i!=j:
            print('своя форма', lst[i][0], ' форма соперника', lst[j][1])
            if lst[i][0]==lst[j][1]:
                print('домашней команде надо переодеться ')
                counter+=1
print(counter)
    # for j in lst:
    #     if i[0]==j[1]:
    #         counter+=1
# print(counter)

