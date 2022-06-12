import multiprocessing


def work1():
    print("work1")


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for i in range(5):
        pool.apply(work1)
