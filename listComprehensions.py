import random
myList = random.sample(range(0, 100), 10)
print(myList)
evenList = []
for element in myList:
    if element % 2 == 0:
        evenList.append(element)
print("The even list is: ", evenList)
