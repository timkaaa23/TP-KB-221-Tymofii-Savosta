def findD(a, b, c):
    D = b**2 - 4 * a * c
    return D

def FindRoots(a, b, c):

	D = findD(a, b, c)

    # D == 0, 1

	if D == 0:
		x1 = -b / (2 * a)
		x2 = x1
	# D > 0, 2

	elif D > 0:
		x1 = -b + D ** 0.5 / (2 * a)
		x2 = -b - D ** 0.5 / (2 * a)

    # D < 0, коренів немає

	else:
		print('Коренів не має')
		exit()

    # if D < 
    # return x1, x2
	return x1, x2


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

x1, x2 = FindRoots(a, b, c)
print(x1, x2)



