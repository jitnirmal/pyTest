class Queue(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item):
		# O(n) operation
        self._items.insert(0,item)

    def dequeue(self):
		# O(1) operation
        return self._items.pop()

    def size(self):
        return len(self._items)

def TestQueue():
	queue = Queue()
	queue.enqueue("first")
	queue.enqueue("second")
	queue.enqueue("third")
	queue.enqueue("fourth")
	
	print(queue.size())
	
	#get the elements
	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.dequeue())
	
	
	
TestQueue()