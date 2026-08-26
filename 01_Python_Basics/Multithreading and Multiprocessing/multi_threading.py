"""import threading

def task():
    print("Task is running")

t1 = threading.Thread(target=task)

t1.start()
t1.join()

print("Main program completed")

import threading
def task():
    print("Task is running")

t1 = threading.Thread(target = task)
t1.start()
t1.join()
print("Single thread-1 works")

import threading

def task():
    print("Task is running")
t1 = threading.Thread(target = task)
t1.start()
t1.join()
print("Single thread-2 works")"""

import threading

def numbers():
    print("Numbers")
t1 = threading.Thread("target = numbers")
t1.start()
t1.join()
print("numbers thread works")