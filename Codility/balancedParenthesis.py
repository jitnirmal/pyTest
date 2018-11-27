def ArePair(opening,closing):
	if opening == '(' and closing == ')':
		return True
	elif opening == '{' and closing == '}': 
		return True
	elif opening == '[' and closing == ']': 
		return True
	return False;


def checkForBalancedParantheses(exp):
	S=[]
	for i in range(len(exp)):
		if (exp[i] == '(' or exp[i] == '{' or exp[i] == '['):
			S.append(exp[i])
		elif (exp[i] == ')' or exp[i] == '}' or exp[i] == ']'):
			if (not S) or (ArePair(S[len(S)-1], exp[i])) == False:
				return False
			else:
				S.pop()
	if not S:
		return True
	else:
		return False


def testParanthesesBalanced():
	expression = "[[]]";
	if (checkForBalancedParantheses(expression)):
		print("Balanced")
	else:
		print("Not Balanced")

testParanthesesBalanced()