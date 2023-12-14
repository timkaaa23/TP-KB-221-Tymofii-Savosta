from sys import argv 
import csv

file_name = argv[0]
csv_file_name = argv[1]

students = []

def printAllList():
    with open(csv_file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
    return

def addNewElement():
    name = input("Please enter student name: ")
    name = name.capitalize()
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")

    with open(csv_file_name, 'a', newline='') as csvfile:
        fieldnames = ['name', 'phone', 'email', 'group']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"name": name, "phone": phone, 'email': email, 'group': group})

    with open(csv_file_name) as reader_file:
        reader = csv.DictReader(reader_file)
        students = list(reader)

    sorted_students = sorted(students, key=lambda row: row['name'])

    with open(csv_file_name, 'w') as csvfile:
        fieldnames = ['name', 'phone', 'email', 'group']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() 
        for row in sorted_students:
            writer.writerow(row) 
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")

    with open(csv_file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)
        students = list(reader)

    for i, row in enumerate(students):
        if row['name'] == name:
            del students[i]
            break

    with open(csv_file_name, 'w', newline='') as csvfile:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in students:
            writer.writerow(row) 
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    with open(csv_file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)
        students = list(reader)


    for i, row in enumerate(students):
        if row['name'] == name:
            new_name = input("Please enter new name: ")
            students[i].update({'name': new_name, 'phone': row['phone'], 'email': row['email'], 'group': row['group']})
            
            sorted_students = sorted(students, key=lambda row: row['name'])
            
            with open(csv_file_name, 'w', newline='') as csvfile:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in sorted_students:
                    writer.writerow(row) 

            break

def main():

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse.upper():
            case "C":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U":
                print("Existing element will be updated")
                updateElement()
            case "D":
                print("Element will be deleted")
                deleteElement()
            case "P":
                print("List will be printed")
                printAllList()
            case "X":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()