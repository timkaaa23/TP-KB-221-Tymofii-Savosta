import csv

names = []

with open("students.txt", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append({"name":row["Name"], "mark":row["Mark"]})


# Сортування по оцінкам
for name in sorted(names, key=lambda elem: elem['mark']):
    print(f"Your name is {name['name']} your mark is {name['mark']}")

print('\n')

# Сортування по імені
for name in sorted(names, key=lambda elem: elem['name']):
    print(f"Your name is {name['name']} your mark is {name['mark']}")