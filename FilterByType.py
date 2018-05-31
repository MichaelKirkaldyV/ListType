

#Write a program that, given some value, tests that value for its type. Here's what you should do for each type:


sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

#You can check to see the data type by using the type(), i.e  print type(aL) will display <type 'List'>
#you can then set the variable equal to a presentType variable 
#i.e presentType = bS
#	 dataType = type(presentType)
#then use if/else statements to check things. 

presentType = bS

dataType = type(presentType)	#if type is printed with 43 it will display type int, so it takes the present type of bI which holds a number
if dataType == int:					#or if isinstance(dataType, int)
	if presentType >= 100:
		print "That's a big number"
	else:
		print "That's a small number"

if dataType == str:				#checks to see if type is Str      #or if isinstance(dataType, str)
	if len(presentType) >= 50:	#takes length of the string type 
		print "Long sentence"
	else:
		print "short sentence"

if dataType == list:
	if len(presentType) >= 10:	#takes length of the list type
		print "Big List"
	else:
		print "Short List"