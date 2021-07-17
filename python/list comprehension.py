myList = [1, 2, 3, 4, 5]
# newList = []

# for x in myList:
#     newList.append(x ** 2)

newList = [x ** 2 for x in myList if x**2%2==0]

print(newList)