import threading
import time

#Define a subclass of the threading.Thread class in our program
#Override the default __init__(self [,args]) method inside the subclass to add in custom arguments for the class
#Override the default run(self [,args]) method inside the subclass to customize the behavior of the thread class when a new thread is initialized and started

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print('Starting thread %s.' % self.name)
        thread_count_down(self.name, self.delay)
        print('Finished thread %s.' % self.name)

def thread_count_down(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)
        print('Thread %s counting down: %i...' % (name, counter))
        counter -= 1
		
		
def TestThread():
	thread1 = MyThread('A', 0.5)
	thread2 = MyThread('B', 0.5)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()
	print('Finished.')
	

TestThread()