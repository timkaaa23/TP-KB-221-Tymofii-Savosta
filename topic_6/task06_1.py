import csv

def sort_by_name(elem):
    return elem['name']
    
names = []

with open("students.txt", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append({"name":row["Name"], "mark":row["Mark"]})

for name in sorted(names, key=lambda elem: elem['mark']):
    print(f"Your name is {name['name']} your mark is {name['mark']}")