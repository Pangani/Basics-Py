import threading
import math
import queue

q = queue.Queue()
threads = []

def worker():
    while True:
        num = q.get()
        if num is None:
            break
        print(f"Processing: {num}")
        result = math.sqrt(num)
        print(f"Result: {result}")
        q.task_done()