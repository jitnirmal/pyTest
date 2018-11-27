
# -- Lists and tuples are a class of data structures called “arrays”. 
# -- Arrays are simply a flat list of data which  can be retrieved in O(1)
# -- lists are dynamic arrays while tuples are static arrays.

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


def TestList():
	thislist = ["apple", "banana", "cherry"]
	print(thislist)
	
	#Print the second item of the list:
	print(thislist[1])
	
	#change the second element
	thislist[1] = "blackcurrant"
	print(thislist)
	
	#loop through list
	for x in thislist:
		print (x)
	
	#check if the item exists
	if "apple" in thislist:
		print("Yes, 'apple' is in the fruits list")
		
	# check the lenght of list
	print(len(thislist))
	
	#append items
	thislist.append("mangoes")
	print(thislist)
	
	#remove items
	thislist.remove("apple")
	print(thislist)
	
	#remove the last item
	thislist.pop()
	print(thislist)
	
	#delete specific items
	del thislist[0]
	print(thislist)
	
	thislist.clear()
	print(thislist)
	
	#recreates
	intlist = list((1,12,9,4,13,5,7,3,2))
	print(intlist)
	
	#sort the list
	intlist.sort()
	print(intlist)
	
	#reverse sort
	intlist.sort(reverse=True)
	print(intlist)
	
	#copy of the list
	listCopy = intlist.copy()
	print(listCopy)
	
	
	
TestList()