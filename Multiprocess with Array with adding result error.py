from multiprocessing import Process, Value, Array, Lock
import os
import time

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            numbers[i] += 1

if __name__ == '__main__':
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at the beginning is: ', shared_array[:])

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at the end is: ', shared_array[:])