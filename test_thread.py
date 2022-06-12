import threading
import time


def sayHello():
    print("Hello")
    print("thread of sayHello:", threading.current_thread().getName())
    time.sleep(2)


def sayHi():
    print("Hi")
    print("thread of sayHi:", threading.current_thread().getName())
    time.sleep(2)


thread_obj1 = threading.Thread(target=sayHello)
thread_obj2 = threading.Thread(target=sayHi)
thread_obj1.start()
thread_obj2.start()

thread_num = len(threading.enumerate())
print("线程数量：", thread_num)
for i in range(thread_num):
    print("线程：", threading.enumerate()[i].getName())

print("线程数量读取完毕")
