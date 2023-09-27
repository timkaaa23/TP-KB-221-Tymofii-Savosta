# Task 1

print('Task 1:' + '\n')

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

def discriminant(a, b, c):
	D = b**2 - 4 * a * c
	return D

D = discriminant(a, b, c)

if D > 0:
	X1 = ((-1 * b) + (D ** 0.5)) / 2 * a
	X2 = ((-1 * b) - (D ** 0.5)) / 2 * a
	print(str(a) + 'x**2 + ' + str(b) + 'x + ' + str(c) + ' = 0\nD = ' + str(D) + '\nX1 = ' + str(X1) + '\nX2 = ' + str(X2))
elif D == 0:
	X = ((-1 * b) / 2 * a)
	print(str(a) + 'x**2 + ' + str(b) + 'x + ' + str(c) + ' = 0\nD = ' + str(D) + '\nX = ' + str(X))
else:
	print('Корней не существует!')