"""из файла json находим номер группы с наибольшим количеством женщин, рожденных после 1977 года"""
import json

with open('group_people.json', 'r') as file:
    data = json.load(file)

# print(data)
result = []
for group in data:
    # обнуляем счетчик женщин для очередной группы group
    female1977 = 0
    # print(group)

    # считаем количество женщин младше 1977
    for human in group['people']:

        # берем очередного человека из группы group
        # print(human)
        if human['gender'] == 'Female' and human['year'] > 1977:
            print(human)
            female1977 += 1
    # в result добавляем элемент, состоящий из списка (номер группы и количество females 1977 года)
    result.append([group['id_group'], female1977])
    print()

# сортируем по второму элементу female1977 в обратном порядке
result.sort(key=lambda x: x[1], reverse=True)
print(*result[0])
