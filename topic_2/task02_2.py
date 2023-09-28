a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = input("Operation: ")

# + - * /
def sum(a,b):
    return a + b

def minus(a,b):
	return a - b 

def mult(a, b):
	return a * b 

def div(a, b):
	return a / b

if op == "+":
    result = sum(a,b)
elif op == "-":
    result = minus(a,b)
elif op == '*':
	result = mult(a,b)
elif op == '/': 
	result = div(a,b)
else:
	print('Оберіть коректну операцію!')

print(result)
