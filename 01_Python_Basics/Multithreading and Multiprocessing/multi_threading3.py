"""import threading
import time

def task(name):
    for i in range(5):
        print(f"{name}: {i}")
        time.sleep(1)

t1 = threading.Thread(target = task, args=("Thread 1",))
t2 = threading.Thread(target = task, args=("Thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Main program completed")

import threading
import time

def task(name):
    for i in range(5):
        print(f"{name}: {i}")
        time.sleep(1)
t1 = threading.Thread(target = task, args = ("Thread1",))
t2 = threading.Thread(target = task, args = ("Thread2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Main program completed")"""

import threading
import time
def task(name):
    for i in range(6):
        print(f"{name}: {i}")
        time.sleep(1)
t1 = threading.Thread(target = task, args = ("Thread1",))
t2 = threading.Thread(target = task, args = ("Thread2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Main program completed")