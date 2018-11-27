class Deque(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0,item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

def TestDeque():
	deque = Deque()
	deque.add_front("first")
	deque.add_rear("second")
	deque.add_rear("third")
	deque.add_rear("fourth")
	
	print(deque.size())
	
	#get the elements
	print(deque.remove_rear())
	print(deque.remove_rear())
	print(deque.remove_rear())
	print(deque.remove_rear())
	
	
	
TestDeque()