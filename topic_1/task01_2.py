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

