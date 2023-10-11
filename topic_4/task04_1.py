while True:
	try:
		a = int(input("Enter a: "))
		b = int(input("Enter b: "))
	except:
		print('Ви повинні використовувати числа!')
		continue
	op = input("Operation: ")

	# + - * /
	def sum(a,b):
	    return a + b

	def minus(a,b):
		return a - b 

	def mult(a, b):
		return a * b 

	def div(a, b):
		
		return a / b
		

	match op:
		case '+':
			result = sum(a,b)
		case '-':
			result = minus(a,b)
		case '*':
			result = mult(a,b)
		case '/':
			try:
				result = div(a,b)
			except:
				print('На нуль ділити не можна!')
				continue
		case _:
			print('Оберіть коректну операцію!')

	print(result)

	ext = input('Type E to exit: ')
	if ext == 'E':
		exit()
