

newListTwo = []
newList = []
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
for value in x:
	if value < 10:
		newList.append(value)
	elif value >= 10:
		newListTwo.append(value)

newList.append(newListTwo)
print newList