def TestDict():
	thisdict =	{"brand": "Ford", "model": "Mustang", "year": 1964 }
	print (thisdict)

	# accessing elements
	x = thisdict["model"]
	print(x)

	x = thisdict.get("model")
	print(x)	


	#change values
	thisdict["year"] = 2018
	print(thisdict)

	thisdict.clear()
	print(thisdict)


TestDict()