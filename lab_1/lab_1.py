# lab_1
helplist = ['1' , '2', '3', '4']

students_dir = {

	'Tymofii Savosta': {'Номер телефону': '+380 93 020 74 42',
						'Eлектронна пошта': 'timka023@icloud.com',
						'Адреса': 'Чернигів, Пухова 115, кв. 1',
						'Кафедра': 'Кафедра кібербезпеки й математичного моделювання',
						'Група': 'КБ221'}, 
	}

def key_by_val(the_dict, value):
	global KEY 
	for key, val in the_dict.items():
		if key == value:
			KEY = key

def main():
	global students_dir
	operations = input('Оберіть операцію:\n1) Подивитись довідник\n2) Додати студента\n3) Змінити дані студента\n4) Видалити студента\n\n9) Вихід\n\n')
		
	match operations:
		case '1':
			a = 1
			for i in students_dir:
				
				print('\n', a, i + ':')
				a += 1
				for j in students_dir[i]:

					key_by_val(students_dir[i], j),
					print('\t', KEY, ' - ', students_dir[i][j])
		case '2':
			new_key 	= input("Уведіть ім'я студента: ")
			phone_num 	= input('Уведіть номер телефону студента: ')
			email 		= input('Уведіть електронну пошту студента: ')
			adress 		= input('Уведіть адресу студента: ')
			department 	= input('Уведіть кафедру студента: ')
			group 		= input('Уведіть групу студента: ')

			students_dir[new_key] = {	
					'Номер телефону': phone_num,
					'Электронна пошта': email,
					'Адреса': adress,
					'Кафедра': department,
					'Група': group} 

			students_dir = dict(sorted(students_dir.items()))	
		case '3':
			step_1 = input("Оберіть номер студента, дані якого треба змінити: ")

			try:
				if int(step_1) > len(students_dir) or int(step_1) < 1:
					print('Такого номера не існує!')
					main()

			except:
				print('Такого номера не існує!')
				main()

			nummer = 1
			OLD_KEY = ''
			for i in students_dir:
				if nummer == int(step_1):
					OLD_KEY = i
				else: nummer += 1

			print('\n' + OLD_KEY + '\n')
			step_2 = input("Оберіть дані студента, які треба змінити:\n1) Ім'я\n2) Номер телефону\n3) Електронна пошта\n4) Адреса\n5) Кафедра\n6) Група\n")
			try:
				if int(step_2) > 6 or int(step_1) < 1:
					print('Такого номера не існує!')
					main()
			except:
				print('Такого номера не існує!')
				main()

			match step_2:
				case '1':
					new_name = input("Уведіть нове ім'я: ")
					students_dir[new_name] = students_dir[OLD_KEY]
					del students_dir[OLD_KEY]
					students_dir = dict(sorted(students_dir.items()))	
				case '2':
					new_phone = input("Уведіть новий номер телефону: ")
					students_dir[OLD_KEY]['Номер телефону'] = new_phone

				case '3':
					new_email = input("Уведіть нову електронну пошту: ")
					students_dir[OLD_KEY]['Електронна пошта'] = new_email
				case '4':
					new_adress = input("Уведіть нову адресу: ")
					students_dir[OLD_KEY]['Адреса'] = new_adress
				case '5':
					new_department = input("Уведіть нову кафедру: ")
					students_dir[OLD_KEY]['Кафедра'] = new_department
				case '6':
					new_group = input("Уведіть нову групу: ")
					students_dir[OLD_KEY]['Група'] = new_group

			print('\n\tРезультат збереженний!\n')

		case '4':
			stud_num = input("Оберіть номер студента, якого потребно видалити: ")
			try:
				if int(stud_num) > len(students_dir) or int(stud_num) < 1:
					print('Такого номера не існує!')
					main()

			except:
				print('Такого номера не існує!')
				main()

			nummer = 1
			for i in students_dir:
				if nummer == int(stud_num):
					break
				else: nummer += 1

			del students_dir[i]
			print('\nСтудент видаленний!\n')

		case '9':
			exit()

		case _:
			print("\nОберіть коректну операцію!\n")
			main() 

	
			
	print('\n\n')
	main()



if __name__ == '__main__':
	main()