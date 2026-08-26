import multiprocessing

def calculate(number):
    total = 0
    for i in range(1, 5_000_001):
        total +=i * number

    print(f"Process {number} completed")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=calculate, args=(1,))
    p2 = multiprocessing.Process(target=calculate, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("All processes completed")