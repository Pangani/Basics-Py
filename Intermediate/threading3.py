import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print(f"{thread_number}Accessing thread...")
    semaphore.acquire()
    print(f"{thread_number} acquired semaphore")
    print(f"{thread_number} waiting 5 seconds")
    time.sleep(5)

    print(f"{thread_number} releasing semaphore")
    semaphore.release()


event = threading.Event()

def function():
    print(f"waiting for event...")
    event.wait()
    print("Continuing")

thread = threading.Thread(target=function)

thread.start()

x = input("Trigger event?")
if(x == "yes"):
    event.set()