class Group_list:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)
        self.students.sort(key=lambda x: x.name)

    def delete(self, name):
        self.students = [studs for studs in self.students if studs.name != name]

    def update(self, name, field, new_value):
        for student in self.students:
            if student.name == name:
                if field == 'name':
                    student.name = new_value
                elif field == 'phone':
                    student.phone = new_value
                elif field == 'email':
                    student.email = new_value
                elif field == 'group':
                    student.group = new_value
                else:
                    print(f'Error: can`t fine field {field}')
                break
        self.students.sort(key=lambda x: x.name)

    def print_all(self):
        for student in self.students:
            print(f'Name: {student.name}, Phone: {student.phone}, E-mail: {student.email}, Group: {student.group}')