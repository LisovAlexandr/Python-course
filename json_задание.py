import json
with open('manager_sales.json','r') as file:
    data = json.load(file)

max_sale=0
name=''
last_name=''
sum_sale=0
for i in data:
    # print(i)
    # print(i['manager']['first_name'])

    if len(i['cars'])>max_sale:
        max_sale=len(i['cars'])

        name=i['manager']['first_name']
        last_name=i['manager']['last_name']

        for car in i['cars']:
            sum_sale+=car['price']

    # for car in i['cars']:
    #     # prinnt(car['price'])
    #     sum+=car['price']
    # sale_count[i['manager']['first_name']]=f"{len(i['cars'])} на сумму {sum}"
    # sale_count['sale_price']=i['cars']['price']


print(name, last_name, sum_sale)