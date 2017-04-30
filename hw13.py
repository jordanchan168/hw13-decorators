import time

def timelog(f):
    def inner(*arg):
        t1 = time.time()
        ans = f(*arg)
        t2 = time.time()
        print "execution time: " + str(t2-t1)
        return ans
    return inner
    
def fnlog(f):
    def inner(*arg):
        print f.func_name + "(" + str(*arg) + ")"
        return f(*arg)
    return inner

#@timelog
@fnlog
def fib(n):
    if n < 2:
        return 1
    return fib(n-2)+fib(n-1)
    
print fib(3)
