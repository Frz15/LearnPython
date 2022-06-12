import multiprocessing
import time


def work1(m_queue):
    for i in range(10):
        m_queue.put("hello work1:" + str(i))
        time.sleep(0.5)


def work2(m_queue):
    for i in range(10):
        print(m_queue.get())
        time.sleep(0.5)


if __name__ == '__main__':
    queue_for_com = multiprocessing.Queue(10)
    process_obj1 = multiprocessing.Process(target=work1, args=(queue_for_com,))
    process_obj2 = multiprocessing.Process(target=work2, args=(queue_for_com,))
    process_obj1.daemon = True
    process_obj2.daemon = True
    process_obj1.start()
    time.sleep(3)
    process_obj2.start()
    time.sleep(5)
    print("main: over")
    exit()
