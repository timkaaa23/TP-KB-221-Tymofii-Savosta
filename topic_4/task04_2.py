try:
	print('\nImportError')
	import main
except ImportError:
	print('There is no main module')

try:
	print('\nValeuError')
	a = int(input('Уведіть число: '))
except ValueError:
	print('Ви маєете ввести число\n')

try:
	print('TypeError')
	string = 'fds'
	integer = 4
	result = string + integer
except TypeError:
	print('Не можна здійснювати математичні дії з різними типами даних')

try:
	print('\nFileNotFoundError')
	with open('main.py', 'r') as file:
		for line in file:
			exec(line)
except FileNotFoundError as e:
    print("Файл не знайденний")
