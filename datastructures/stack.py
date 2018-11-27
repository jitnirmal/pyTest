class Stack(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

def TestStack():
	stack = Stack()
	stack.push("first")
	stack.push("second")
	stack.push("third")
	stack.push("fourth")
	
	print(stack.size())
	
	#get the elements
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	
	
	
TestStack()