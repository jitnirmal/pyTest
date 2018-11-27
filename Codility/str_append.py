
def strAppend(str1,str2):
	len1 = len(str1)
	len2 = len(str2)

	minLen = min(len1,len2)

	retStr=''
	index=0
	for i in range(minLen):
		retStr += (str1[i])
		retStr += (str2[i])
		index += 1

	if len1 > len2:
		retStr += str1[index:]
	else:
		retStr += str2[index:]

	return retStr

def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):
    	# copy the string (store as array)
        string_copy = [ch for ch in string]
        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)

#print(strAppend("nrajt singh","imli"))
permutations("ABCD")