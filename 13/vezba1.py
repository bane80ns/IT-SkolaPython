import time
import threading

def writeHello():
    while True:
        print("Hello World")
        time.sleep(5)


thread_hello = threading.Thread(target=writeHello)
thread_hello.start()


print("Prosao petlju")