
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", 'email': 'Bob06@gmail.com', 'group': 'KB221'},
    {"name":"Emma", "phone":"0631234567", 'email': 'Emma@gmail.com', 'group': 'KB222'},
    {"name":"Jon",  "phone":"0631234567", 'email': 'jonwatson@gmail.com', 'group': 'AM211'},
    {"name":"Zak",  "phone":"0631234567", 'email': 'isaak@gmail.com', 'group': 'KI105'}
]

def printAllList():
    for elem in list:
        strForPrint = f"Student name is {elem['name']},  Phone is {elem['phone']}, E-mail is {elem['email']}, Group is {elem['group']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    name = name.capitalize()
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, 'email': email, 'group': group}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
	name = input("Please enter name to be updated: ")
	counter = 0
	for elem in list:
		if elem['name'] == name:
			new_name = input("Pease enter new student name: ")
			new_name = new_name.capitalize()

			elem['name'] = new_name
			print(elem)

			insertPosition = 0
			for item in list:
				if new_name > item["name"]:
					insertPosition += 1
				elif new_name < item['name']:
					break
			list.insert(insertPosition, list.pop(counter))
			print("Element has been changed")
			return
		counter += 1
    # implementation required

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse.upper():
            case "C":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U":
                print("Existing element will be updated")
                updateElement()
            case "D":
                print("Element will be deleted")
                deleteElement()
            case "P":
                print("List will be printed")
                printAllList()
            case "X":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()