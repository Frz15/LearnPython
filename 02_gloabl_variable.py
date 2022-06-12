import threading
import time


g_num = 1

def work1():
    global g_num
    for i in range(1000000):
        g_num = g_num + 1
    print("work1:", g_num)


def work2():
    global g_num
    for i in range(1000000):
        g_num = g_num + 1
    print("work2:", g_num)


if __name__ == '__main__':
    thread_obj1 = threading.Thread(target=work1)
    thread_obj2 = threading.Thread(target=work2)

    thread_obj1.start()
    thread_obj2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(0.5)
    print("main:", g_num)

