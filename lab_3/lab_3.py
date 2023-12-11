from sys import argv 
import csv
from student import Student
from group_list import Group_list
from filehandler import FileHandler

file_name = argv[0]
csv_file_name = argv[1]

def main():

    while True:
            choice = input("Choose action [ C create, U update, D delete, P print list,  X exit ] ")
            student_group = FileHandler.read_from_file(csv_file_name)

            if choice.upper() == "C":
                print("New element will be created:")

                name = input("Enter name: ")
                phone = input("Enter phonenumber: ")
                email = input("Enter e-mail: ")
                group = input("Enter group: ")

                student = Student(name, phone, email, group)
                student_group.add(student)

                FileHandler.write_to_file(csv_file_name, student_group)
                student_group.print_all()

            elif choice.upper() == "U":
                print("An element will be updated")

                name = input("Enter name for update: ")
                field = input("Enter field to update: ")
                new_value = input('Enter new value: ')

                student_group.update(name, field, new_value)
                FileHandler.write_to_file(csv_file_name, student_group)

            elif choice.upper() == "D":
                print("An element will be deleted")

                name = input("Enter name to delete: ")

                student_group.delete(name)
                FileHandler.write_to_file(csv_file_name, student_group)

            elif choice.upper() == "P":

                print("The list will be printed")

                student_group.print_all()

            elif choice.upper() == "X":
                print("Exit()")
                break
            else:
                print("Wrong choice")



main()