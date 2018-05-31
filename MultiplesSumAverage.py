
#Multiples
#Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.


for element in range(1,1001): 	#prints each element in range of 1-1001 in order to include 1000
	print element

#----------------------------------------------------------------#

#Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

for element in range(5,1000001):	#range from 5-1,000,001 to include 1,000,000
	if element % 5 == 0:		#if number is divisible by 5 evenly then print the element 
		print element


#or
for count in range(5,1000001,5):	#3rd number says to count by 5.
    print count

#----------------------------------------------------------------#


#Sum List
#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]


total = 0
a = [1, 2, 5, 10, 255, 3]
for element in a:
	total+=element

print total

#----------------------------------------------------------------#

#Average List
#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]


average = 0
total = 0
a = [1, 2, 5, 10, 255, 3]
for element in a:
	total+=element

average = total/len(a)
print average


