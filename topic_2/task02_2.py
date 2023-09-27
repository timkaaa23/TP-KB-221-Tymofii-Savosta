# Task 2

print('Task 2:' + '\n')

helplist = ['1' , '2', '3', '4', '5', '6']

def main():
	operation = input('\n\nВведите номер операции, которую хотите сделать: \n1) Добавление\n2) Вычитание\n3) Умножение\n4) Деление\n5) Возвести в степень \n6) Деление по модулю\n\n9) Выход\n\n')

	if operation == '9':
		exit()
	elif operation not in helplist:
		print("\nВведите коректную операцию!\n")
		main() 

	try:
		a = float(input("Введите первое число: "))
		b = float(input("Введите второе число: "))
	except:
		print('\nТребуется вводить числа!\n')
		main()

	if operation == '1':
		print(a + b)
	elif operation == '2':
		print(a - b)
	elif operation == '3':
		print(a * b)
	elif operation == '4':
		print(a / b)
	elif operation == '5':
		print(a ** b)
	elif operation == '6':
		print(a % b)

	main()
if __name__ == '__main__':
	main()



