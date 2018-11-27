import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        counter = 10

        while counter:
            time.sleep(self.delay)
            print('Thread %s counting down: %i...' % (self.name, counter))
            counter -= 1


def TestThread():
	thread1 = MyThread('A', 0.5)
	thread1.start()
	thread1.join()
	print('Finished.')


TestThread()
