import socket
from queue import Queue
import threading

queue = Queue()
target = "10.0.0.5"

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False

def worker():
    while True:
        port = queue.get()
        if scan_port(port):
            print(f"Port {port} is open.")
        queue.task_done()

for i in range(1, 501):
    queue.put(i)

for i in range(30):
    t = threading.Thread(target=worker)
    t.start()

    
