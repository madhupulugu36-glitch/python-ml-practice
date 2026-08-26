import multiprocessing

def task(name):
    print(f"{name} is running")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task, args=("Process 1",))
    p2 = multiprocessing.Process(target=task, args=("Process 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main program completed")