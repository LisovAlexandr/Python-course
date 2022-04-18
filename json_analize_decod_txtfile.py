import json

with open('Alphabet.json', 'r') as file:
    keys = json.load(file)
# print(keys)
with open('Abracadabra.txt', 'r') as file2:
    text = file2.read()
# print(text)
# print()
for char in text:
    if char in keys:
        char = char.replace(char,keys[char])
        print(char, end='')
    else:
        print(char, end='')

