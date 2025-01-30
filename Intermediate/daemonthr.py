import threading
import time

path = "text.txt"
text = ""

def read_file():
    global text, path
    while True:
        with open(path) as f:
            text = f.read()
        time.sleep(3)

def printloop():
    global text
    for i in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=read_file, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()