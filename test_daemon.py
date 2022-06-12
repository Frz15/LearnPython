import threading
import time


def thread_work():
    for i in range(5):
        print("Hello")
        time.sleep(1)


if __name__ == '__main__':
    thread_obj = threading.Thread(target=thread_work)
    thread_obj.setDaemon(True)
    thread_obj.start()
    print("main hello")
    time.sleep(2)
    exit()


