import time 
from threading import Thread


def do_that():
    print("Starting That! ")
    time.sleep(2)
    print("Did that")

def do_this():
    print("Starting This! ")
    time.sleep(3)
    print("Did this")



t1 = Thread(target=do_that)
t1.start()

t2= Thread(target=do_this)
t2.start()
