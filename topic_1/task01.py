# Task 1 

print('Task 1:' + '\n')

task1_string = 'abcdefg123'
res = ''

for i in task1_string:
	res += task1_string[-1]
	task1_string = task1_string[:-1]
	print(task1_string + ' - ' + res + '\n')

# Task 2

print('Task 2:' + '\n')

# strip() 

print('• strip()' + '\n')

task2_string = 'bla bla bla 123 123 123 this task is too ez'

print(task2_string.strip('bla') + '\n')
print(task2_string.strip(' bla') + '\n')
print(task2_string.strip('thi') + '\n')

# capitalize() 

print('• capitalize()' + '\n')

name, surname = 'tYMofIi', "sAVOstA"

print(name.capitalize(), surname.capitalize()  + '\n')

# title() 

print('• title()' + '\n')

full_name = 'saVOsTa tymoFII serGeiviCH'

print(full_name.title() + '\n')

# upper() and lower()

print('• upper() and lower()' + '\n')

new_string = 'THIS is Test sTRING for METHODs upper() AND lower()'

print(new_string.lower() + ' - ' + new_string.upper() + '\n')

# split() and join()

print('• split() and join()' + '\n')

task2_2_string = 'orange tomato banana potato cheese milk'
splited_list = task2_2_string.split()
print(splited_list)
joined_string = '; '.join(splited_list)
print('\n' + joined_string + '\n')

# Task 3

print('Task 3:' + '\n')

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

def discriminant(a, b, c):
	D = b**2 - 4 * a * c
	return D

D = discriminant(a, b, c)

X1 = ((-1 * b) + (D ** 0.5)) / 2 * a
X2 = ((-1 * b) - (D ** 0.5)) / 2 * a

print(str(a) + 'x**2 + ' + str(b) + 'x + ' + str(c) + ' = 0\nD = ' + str(D) + '\nX1 = ' + str(X1) + '\nX2 = ' + str(X2))