# extend()

print('\nextend()\n')

task_list = [-1, '1', 'orange']

print(task_list)

task_list.extend('4')

print(task_list)

new_list = [999, 'task2']

task_list.extend(new_list)

print(task_list)

# append()

print('\nappend()\n')

task_list.append(5)
task_list.append('90')

print(task_list)

# insert(id, val)

print('\ninsert()\n')

task_list.insert(0, 'number 1')
task_list.insert(4, 'number 5')

print(task_list)

# remove(val)

print('\nremove()\n')

task_list.remove(5)
task_list.remove('task2')

print(task_list)

# clear()

print('\nclear()\n')

task_list.clear()

print(task_list)

# sort()

task_list = [9, 99, 87, 4, 0, 41]

print('\nsort()\n')

task_list.sort()

print(task_list)

# reverse()

print('\nreverse()\n')

task_list.reverse()

print(task_list)

# copy()

print('\ncopy()\n')

copy_list = task_list.copy()

print(copy_list)

