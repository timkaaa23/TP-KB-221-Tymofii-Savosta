from sys import argv 
import csv
import unittest, os 
from unittest.mock import patch
from io import StringIO

csv_file_name = 'test_students.csv'

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

class Test_book(unittest.TestCase):

    def setUp(self):
        self.csv_file_name = 'test_students.csv'
        self.fieldnames = ['name', 'phone', 'email', 'group']
        self.students_data = [
            {'name': 'Alice', 'phone': '413423434', 'email': 'alice@google.com', 'group': 'fsdf324'},
            {'name': 'Bob', 'phone': '41242423', 'email': 'bob@apple.com', 'group': 'sdf2534'}
        ]
        with open(self.csv_file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            for student in self.students_data:
                writer.writerow(student)

    def tearDown(self):
        os.remove(self.csv_file_name)

    def test_add_new_element(self):
        with patch('builtins.input', side_effect=['timka', '1341234', 'timka@icloud.com', 'KB221']):
            addNewElement()
            with open(self.csv_file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                new_students = list(reader)
            self.assertEqual(len(new_students), len(self.students_data) + 1)

    def test_delete_element(self):
        with patch('builtins.input', side_effect=['Bob']):
            deleteElement()
            with open(self.csv_file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                new_students = list(reader)
            self.assertEqual(len(new_students), len(self.students_data) - 1)

    def test_update_element(self):
        with patch('builtins.input', side_effect=['Alice', 'timka']):
            updateElement()
            with open(self.csv_file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                updated_students = list(reader)
            updated_names = [student['name'] for student in updated_students]
            self.assertIn('timka', updated_names)
            self.assertNotIn('Alice', updated_names)

    def test_print_all_list(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            printAllList()
            output = mock_stdout.getvalue().strip()
            for student in self.students_data:
                self.assertIn(student['name'], output)
                
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
