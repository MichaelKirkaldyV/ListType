
'''
In this string: words = "It's thanksgiving day. It's my birthday,too!" 
print the position of the first instance of the word "day". 
Then create a new string where the word "day" is replaced with the word "month".
'''
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")

#-----------------------------------------------------------------#

#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

numbers = [15,9,90,6,3,1]
print max(numbers)
print min(numbers)

#------------------------------------------------------------------#

'''
First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. 
Now create a new list containing only the first and last values in the original list. Your code should work for any list.
'''

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[7]

#------------------------------------------------------------------#

"""
New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. 
Push the list created from the first half to position 0 of the list created from the second half. 
The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
"""

newListTwo = []				#creates a new list
newList = []
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()						#sorts the values of x from low to high
print x
for value in x:
	if value < 10:
		newList.append(value)	#adds the value of x into the newlist
	elif value >= 10:
		newListTwo.append(value)		#adds the value of x into the 2nd list

newList.append(newListTwo)			#appends the 2nd list inside the end of the first list 
print newListTwo					#Prints the new list


