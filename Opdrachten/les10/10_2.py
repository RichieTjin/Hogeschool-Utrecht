b = 7

def verdubbelB():
    global b
    b = b + b

verdubbelB()
print (b)





import time

t = (2017, 22, 10, 1, 2, 4, 5, 6, 7)
t = time.mktime(t)
print(time.strftime("%H:%M:%S", time.gmtime(t)))





def f(y):
    return (2*y) + 1

def g(x):
    return 5 + x + 10

print(f(3)+g(3))