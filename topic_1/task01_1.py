# Task 1 

print('Task 1:' + '\n')

task1_string = 'abcdefg123'
res = ''

for i in task1_string:
	res += task1_string[-1]
	task1_string = task1_string[:-1]
	print(task1_string + ' - ' + res + '\n')
