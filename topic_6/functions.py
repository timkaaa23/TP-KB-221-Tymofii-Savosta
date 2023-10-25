def sum(a,b):
    return a + b

def minus(a,b):
	return a - b 

def mult(a, b):
	return a * b 

def div(a, b):
	try:
		return a / b
	except:
		print('На нуль ділити не можна!')

if __name__ == '__main__':
	print('Ви запустили цей файл, як головний!\n')
elif __name__ == 'functions':
	print('Дякуємо за використання модуля обчислення!\n')