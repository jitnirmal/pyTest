# All variables have a type that can be seen by using the built-in type() function.

def testTypes():
	print(type(23))
	print(type('nirmal'))

	#Integer numbers have no realistic limit
	v = 123672879878279864982374982348237429384
	result = v*v
	print(result)
	print(type(result))

	#Real numbers (i.e., those with decimal points) are stored with what is called double-precision. For example:
	fl = 1 / 7.0;
	print(type(fl)) #float
	print(fl)

	print(int(2.34))
	print(float(2))
	print(bool(2))

def testStrings():
	"""Strings : A sequence of characters that together form a text string.
	The elements of a sequence are stored as a contiguous series of memory locations. 
	The first element in the sequence can be accessed at position 0 and the last element at position n – 1 
	"""

	catString = 'Nirmal'+'jit'+' '+'Singh'
	print(catString)
	print(catString[0:6])
	print(catString.upper())
	print('jit' in catString)

	name="Samar"
	age=8
	str2 = '%s is %d years old' % (name,age)
	print(str2)

	print('%s is %d years old' % (name,age))

	'''
		%c : Single character/string of length 1
		%s : String
		%d : Signed decimal integer
		%f : Floating point number
		%% : Percent character
	'''

testTypes()
testStrings()