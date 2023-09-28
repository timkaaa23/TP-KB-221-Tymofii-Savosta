# Task 3

# aX**2 + bX + c = 0
# D = b**2 - 4ac

# x1 = (-b + sqrt(D))/2*a
# x2 = (-b - sqrt(D))/2*a

def findD(a, b, c):
	D = b**2 - 4 * a * c

	x1 = (-b + D ** 0.5) / 2*a
	x2 = (-b - D ** 0.5) / 2*a
    # ...
    # return 

	return x1, x2

a = int(input("Please enter start point: "))
b = int(input("Please end point: "))
c = int(input("please enter mult: "))

print(findD(a, b,c))