# update()

print('\nupdate()\n')

task_dict = {'fruits': ['orange', 'apple', 'anannas', 'banana'],
			 'vegetables': ['cucumber', 'tomato', 'potato', 'carrot'],
			 'meat': ['chiken', 'steak', 'beaf', 'fish']}

for i in task_dict:
	print(i, task_dict[i])


new_dict = {'drink': ['tea', 'coffee', 'water', 'cola']}

task_dict.update(new_dict)

print('\n//update//\n')

for i in task_dict:
	print(i, task_dict[i])

# del

print('\ndel()\n')

for i in task_dict:
	print(i, task_dict[i])

del task_dict['vegetables']

print('\n//del//\n')

for i in task_dict:
	print(i, task_dict[i])

# clear

print('\nclear()\n')

task_dict.clear()
print(task_dict)

# keys()

task_dict = {'fruits': ['orange', 'apple', 'anannas', 'banana'],
			 'vegetables': ['cucumber', 'tomato', 'potato', 'carrot'],
			 'meat': ['chiken', 'steak', 'beaf', 'fish'],
			 'drink': ['tea', 'coffee', 'water', 'cola']}

print('\nkeys()\n')

for i in task_dict.keys():
	print(i)

# values()

print('\nvalues()\n')

for i in task_dict.values():
	print(i)

# items()

print('\nitems()\n')

for i in task_dict.items():
	print(i)

