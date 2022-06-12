import threading
import time


def work1():
    global g_num
    for i in range(1000000):
        test_mutex.acquire()
        g_num = g_num + 1
        test_mutex.release()
    print("work1:", g_num)


def work2():
    global g_num
    for i in range(1000000):
        test_mutex.acquire()
        g_num = g_num + 1
        test_mutex.release()
    print("work2:", g_num)


if __name__ == '__main__':
    g_num = 0
    test_mutex = threading.Lock()
    thread_obj1 = threading.Thread(target=work1)
    thread_obj2 = threading.Thread(target=work2)
    thread_obj1.start()
    thread_obj2.start()
    while len(threading.enumerate()) != 1:
        time.sleep(0.5)
    print("main:", g_num)
