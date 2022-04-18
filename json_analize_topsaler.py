"""из файла json находим самого успешного продавца по сумме продаж"""
import json

with open('manager_sales.json', 'r') as file:
    data = json.load(file)

print(type(data))
print('в файле', len(data), 'строк')
print()

result = []
for manag in data:
    sum_sale = []
    # print(manag['manager']['first_name'])
    for car in manag['cars']:
        sum_sale.append(car['price'])
        # print(car['price'])
    result.append([manag['manager']['first_name'], manag['manager']['last_name'], sum(sum_sale)])

top_sallers_list = sorted(result, key=lambda x: x[2], reverse=True)
# # вывести весь список продавцов, сортировка по уменьшению суммы продаж
# for i in win:
#     print(*i)

# лучший продавец
print(*top_sallers_list[0])
