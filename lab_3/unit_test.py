import unittest
import csv
import os

from student import Student
from group_list import Group_list
from filehandler import FileHandler

class TestStudent(unittest.TestCase):
    def test_name_capitalization(self):
        student = Student("timka", "4132424", "timka023@icloud.com", "KB221")
        self.assertEqual(student.name, "Timka")

class TestGroupList(unittest.TestCase):
    def setUp(self):
        self.group_list = Group_list()

    def test_add(self):
        student = Student("John", "123", "john@example.com", "group1")
        self.group_list.add(student)
        self.assertEqual(len(self.group_list.students), 1)

    def test_delete(self):
        student = Student("Timka", "4132424", "timka023@icloud.com", "KB221")
        self.group_list.add(student)
        self.group_list.delete("Timka")
        self.assertEqual(len(self.group_list.students), 0)

    def test_update(self):
        student = Student("Timka", "4132424", "timka023@icloud.com", "KB221")
        self.group_list.add(student)
        self.group_list.update("Timka", "phone", "+380 93 020 74 42")
        updated_student = self.group_list.students[0]
        self.assertEqual(updated_student.phone, "+380 93 020 74 42")

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.csv_file_name = "lab_3_unit_test.csv"

    def test_read_from_file(self):
        with open(self.csv_file_name, 'w', newline='') as csvfile:
            fieldnames = ['name', 'phone', 'email', 'group']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name': 'Timka', 'phone': '143423', 'email': 'timka@icloud.com', 'group': 'KB221'})

        student_group = FileHandler.read_from_file(self.csv_file_name)
        self.assertEqual(len(student_group.students), 1)
        self.assertEqual(student_group.students[0].name, "Timka")

    def test_write_to_file(self):
        student = Student("Anna", "3424232", "anna@blablalba.com", "KB221")
        student_group = Group_list()
        student_group.add(student)

        FileHandler.write_to_file(self.csv_file_name, student_group)

        with open(self.csv_file_name, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            written_student = next(reader)

        self.assertEqual(written_student['name'], "Anna")

    def tearDown(self):
        os.remove(self.csv_file_name)

if __name__ == "__main__":
    unittest.main()