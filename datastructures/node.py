class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

		
class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
	
def hash(astring, tablesize):
    the_sum = sum(ord(char) for char in astring)
    return the_sum % tablesize