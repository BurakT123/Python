import time
import random

def func(array):
    t = []
    z = 0

    for i in array:
        if i != 0:
            t.append(i)
        else:
            z += 1
    t.extend(z * [0])
    return t 


n = 20000
arr = [1,0,2,0,2,1,2]
start = time.time()
x = func(arr)
stop = time.time()
print(stop-start)