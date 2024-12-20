from multiprocessing import Process
import os

def square_numbers():
    for i in range(1000):
        i * i

if __name__ == '__main__':
    processes = []
    num_process = os.cpu_count()
    # number of CPUs on the machine. Usually a good choice for the number of processes.

    # create processes and assign a function for each process
    for i in range(num_process):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main program until these processes are finished
    for process in processes:
        process.join()