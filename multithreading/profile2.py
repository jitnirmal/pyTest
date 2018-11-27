#PYTHONPATH : This variable tells the Python interpreter where to locate the module files imported into a program.
#PYTHONHOME : It is an alternative module search path.


from memory_profiler import profile
import time

@profile
def test1():
    n = 10000
    a = [1] * n
    time.sleep(1)
    return a

@profile
def test2():
    n = 100000
    b = [1] * n
    time.sleep(1)
    return b

if __name__ == "__main__":
    test1()
    test2()