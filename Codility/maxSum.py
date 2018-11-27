def getSubArrayMaxSum(arr):
	maxSum = 0;
	maxTillHere = 0;

	for i in range(len(arr)):
		maxTillHere += arr[i];
		if (maxTillHere < 0):
			maxTillHere = 0

		if (maxSum < maxTillHere):
			maxSum = maxTillHere
	
	return maxSum;

def testSubArrayMaxSum():
	arr =[-2, -3, 4, -1, -2, 1, 5, -3]
	print(getSubArrayMaxSum(arr))

testSubArrayMaxSum()