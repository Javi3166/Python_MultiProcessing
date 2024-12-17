from multiprocessing import Pool

def cube(number):
    return number * number * number

if __name__ == '__main__':

    numbers = range(10)
    pool = Pool()

    # map, apply, join, close <- Multiple methods related to pool
    result = pool.map(cube, numbers) # Map will use the maximum number of processes available. It will split the iterable into
                                    # equal size chunks before feeding them to the method and run them all parallel

    # Apply will process one just one if needed for just one instance
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join()

    print(result)