'''как работать с json'''
import json
str_json='''
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    }
  ]
}'''
# из строки json получаем python словарь
data=json.loads(str_json)
##print(type(data))  # dict

# превратим python строку в строку json, inden отступ внутри строки
new_json=json.dumps(data,indent=2)
##print(new_json)    # type str

# преобразуем и сохраним python строку в файл json
with open('my.json','w') as file:
    json.dump(data,file,indent=3)

# прочитаем json из файла и преобразуем в python код
with open('my.json','r') as file2:
    data2 = json.load(file2)
members= data2['members']

for i in members:
    print(i['name'])