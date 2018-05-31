


'''
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. 
If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum.
At the end of your program print the string, the number and an analysis of what the list contains. 
If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?
'''

li = [15,10,"Mike","love",90]
li_two = ["Marcus","Lettecia"]

def listType(list):
	total = 0
	newString = ""

	for data in list:
		if isinstance(data, str):
			newString+=data
		if isinstance(data, int):
			total+=data

	if total and newString:
		print "This is a mixed list"
		print "String: " + newString
		print "total: ", total

	elif newString:
		print "This list is of string type"
		print "String: " + newString
	else:
		print "This list is of integer type"
		print "total: ", total

print listType(li)
	



	
