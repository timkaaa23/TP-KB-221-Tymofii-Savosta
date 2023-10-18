import importlib, functions, operations

while True:

	number_1 = operations.a
	number_2 = operations.b

	operation = operations.op

	result = None

	match operation:
		case '+':
			result = functions.sum(number_1,number_2)
		case '-':
			result = functions.minus(number_1,number_2)
		case '*':
			result = functions.mult(number_1,number_2)
		case '/':
			result = functions.div(number_1,number_2)
		case _:
			print('Оберіть коректну операцію!')

	print(result)

	ext = input('Type E to exit: ')
	if ext == 'E':
		exit()
	else:
		importlib.reload(operations)
