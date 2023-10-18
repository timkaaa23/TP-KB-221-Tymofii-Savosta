while True:
	try:
		a = int(input("Enter a: "))
		b = int(input("Enter b: "))
		op = input("Operation: ")
		break
	except:
		print('Ви повинні використовувати числа!')

if __name__ == '__main__':
	print('Ви запустили цей файл, як головний!\n')
elif __name__ == 'operations':
	print('Дякуємо за використання модуля отримання даних!\n')
	