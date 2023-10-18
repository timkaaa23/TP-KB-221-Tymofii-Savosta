import functions

while True:
	try:
		a = int(input("Enter a: "))
		b = int(input("Enter b: "))
	except:
		print('Ви повинні використовувати числа!')
		continue
	op = input("Operation: ")

	match op:
		case '+':
			result = functions.sum(a,b)
		case '-':
			result = functions.minus(a,b)
		case '*':
			result = functions.mult(a,b)
		case '/':
			try:
				result = functions.div(a,b)
			except:
				print('На нуль ділити не можна!')
				continue
		case _:
			print('Оберіть коректну операцію!')

	print(result)

	ext = input('Type E to exit: ')
	if ext == 'E':
		exit()
