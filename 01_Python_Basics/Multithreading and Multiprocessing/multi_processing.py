import multiprocessing

def task():
    print("Processing is running")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task)
    p1.start()
    p1.join()

    print("Main program completed")