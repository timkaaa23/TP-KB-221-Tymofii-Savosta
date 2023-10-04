while True:
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
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
			result = div(a,b)
		case _:
			print('Оберіть коректну операцію!')

	print(result)

	ext = input('Type E to exit: ')
	if ext == 'E':
		exit()
