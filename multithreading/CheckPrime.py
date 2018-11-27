from math import sqrt
import threading

def is_prime(x):
    if x < 2:
        print('%i is not a prime number.' % x)

    elif x == 2:
        print('%i is a prime number.' % x)

    elif x % 2 == 0:
        print('%i is not a prime number.' % x)

    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print('%i is not a prime number.' % x)

        print('%i is a prime number.' % x)

class MyThread(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x

    def run(self):
        print('Starting processing %i...' % self.x)
        is_prime(self.x)
	
def TestPrime():
    my_input = [2, 193, 323, 1327, 433785907]
    threads = []

    for x in my_input:
        temp_thread = MyThread(x)
        temp_thread.start()
        threads.append(temp_thread)
    for thread in threads:
        thread.join()
    print('Finished.')
	
TestPrime()