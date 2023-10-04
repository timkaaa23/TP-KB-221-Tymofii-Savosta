task_list = ["aa", "ee", "zz"]
print(task_list)

newValue = input("New value: ") 

newValue_list = [newValue]

counter = 0
for i in task_list:
    if newValue < i:
        result = task_list[0:counter] + newValue_list + task_list[counter:]
        counter = 0
    counter += 1

print(result)

