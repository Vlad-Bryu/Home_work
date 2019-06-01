import csv

users = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]

with open('export_users.csv', 'w', encoding='utf-8', newline='') as w:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(w, fields, delimiter=',')
    writer.writeheader()
    for string in users:
        writer.writerow(string)
