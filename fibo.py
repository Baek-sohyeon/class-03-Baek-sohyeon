import time

def fibo(n):
    if n  <= 1:
        return n
    return fibo(n-1)+fibo(n-2)

def iterfibo(n):
    a = 0
    b = 1
    tmp = 0
    if (n == 1):
        return 1
    elif (n == 0):
        return 0
    else:
        for i in range(n-1):
            tmp = a+b
            a = b
            b = tmp
        return tmp

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("iterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))