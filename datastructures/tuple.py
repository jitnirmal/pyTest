

#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# addition,chaging, deleting elements raise error

def TestTuple():
	thistuple = ("apple", "banana", "cherry")
	print(thistuple)
	
	print(thistuple[1])
	
	#Change Tuple Values
	#thistuple[1] = "blackcurrant"
	# interpretor error , tuple' object does not support item assignment
	
	#loop through the tuple
	for x in thistuple:
		print (x)
		
	#check if this item exists
	if "apple" in thistuple:
		 print("Yes, 'apple' is in the fruits tuple") 

	thisList = ['nirmal','singh',2]
	print(thisList)
	
TestTuple()