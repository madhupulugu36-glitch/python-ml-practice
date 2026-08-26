import threading
import time

def task():
    print("Task Started")
    time.sleep(3)
    print("Task completed")

t1 = threading.Thread(target = task)

print("Before start:", t1.is_alive())

t1.start()

print("After start:", t1.is_alive())

t1.join()

print("After join:", t1.is_alive())