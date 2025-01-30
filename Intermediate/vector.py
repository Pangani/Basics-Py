import threading

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "X: %s, y: %s" % (self.x, self.y)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    

def hello():
    print("Hello, World!")

def function():
    for x in range(1000):
        print("ONE")

def function2():
    for x in range(1000):
        print("TWO")

t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function)

t1.start()
t2.start()
t3.start()