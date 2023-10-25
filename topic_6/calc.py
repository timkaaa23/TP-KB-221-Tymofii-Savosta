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

	with open('calc_log.txt', 'a') as log:
		log.write(f'Введені дані:    {number_1} та {number_2}\nОбрана операція: {operation}\nРезультат:       {result}\n{number_1} {operation} {number_2} = {result}\n\n')
		log.close()

	ext = input('Type E to exit: ')
	if ext == 'E':
		exit()
	else:
		importlib.reload(operations)
