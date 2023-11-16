def findMinElemWithIndex(listForSearch:list):
    id = 0
    elem = listForSearch[0]
    counter = 0
    
    for i in listForSearch:
    	if i < elem:
    		elem = i
    		counter = id
    	id += 1

    id = counter
    return id, elem

def findMaxElemWithIndex(listForSearch:list):
    id = 0
    elem = -1
    counter = 0
    for i in listForSearch:
    	if i > elem:
    		elem = i
    		counter = id
    	id += 1
    id = counter
    return id, elem

def main():
    listOfData = [5, 11, 14, 22, 33, 7, 88, 999, 123, -4, 64, 10, 55, 66, 44, 20, 345]
    
    result = findMinElemWithIndex(listOfData)
    print(f"Min id: {result[0]}, Min value: {result[1]}") # 5

    result = findMaxElemWithIndex(listOfData)
    print(f"Max id: {result[0]}, Max value: {result[1]}") # 345

if __name__ == "__main__":
    main()