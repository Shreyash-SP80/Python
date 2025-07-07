# Implement a decorator that caches the return value of the function, so that when it's called with the same arguments, the cached value
#    is returned instead of re-executing the functon

import time

def  cache(func):
    cache_value = {}
    print(cache_value)
    def  wfx(*args):
        if args in cache_value:
            # print(cache_value)    # {(2, 3): 5, (3, 4): 7}
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wfx

@cache
def  long_running_function(a, b):
    time.sleep(4)
    return a + b 

print(long_running_function(2, 3))
print(long_running_function(3, 4))
print(long_running_function(2, 3))
print(long_running_function(3, 4))