import importlib, functions, operations

logs = []

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

	class Logs():
		def __init__(self, number_1, number_2, operation, result):
			self.task = f'{number_1} {operation} {number_2} = {result}'
			logs.append(self.task)

	log = Logs(number_1, number_2, operation, result)

	ext = input('Type E to exit or log to watch logs:' )

	if ext == 'E':
		exit()
	elif ext == 'log':
		print('\n')
		for i in logs:
			print(i)
		importlib.reload(operations)
	else:
		importlib.reload(operations)
