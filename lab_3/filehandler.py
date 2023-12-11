import csv

from student import Student
from group_list import Group_list

class FileHandler:
    @staticmethod
    def read_from_file(csv_file_name):
        student_group = Group_list()
        with open(csv_file_name, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row['name'], row['phone'], row['email'], row['group'])
                student_group.add(student)
        return student_group

    

    @staticmethod
    def write_to_file(csv_file_name, student_group):
        with open(csv_file_name, 'w', newline='') as csvfile:
            fieldnames = ['name', 'phone', 'email', 'group']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_group.students:
                writer.writerow({'name': student.name, 'phone': student.phone, 'email': student.email, 'group': student.group})

