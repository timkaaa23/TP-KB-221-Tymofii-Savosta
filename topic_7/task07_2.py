import csv

names = []

class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

        names.append({"name": name, "age": age})

stud1 = Student('Timka', 19)
stud2 = Student('Lilia', 16)
stud4 = Student('Vova', 25)
stud3 = Student('Alex', 20)

# Сортування по віку
for name in sorted(names, key=lambda elem: elem['age']):
    print(f"Your name is {name['name']} your age is {name['age']}")

print('\n')

# Сортування по імені
for name in sorted(names, key=lambda elem: elem['name']):
    print(f"Your name is {name['name']} your age is {name['age']}")