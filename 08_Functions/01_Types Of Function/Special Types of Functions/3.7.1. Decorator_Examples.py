import time

def  timer(func):
    def wfx(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Total time taken by {func.__name__} function: {end - start:.2f}")
    return wfx

@timer
def  add(a, b):
    print(f"Addition: {a+b}")

@timer
def  take_Time(n):
    time.sleep(n)

take_Time(2)
add(10, 20)

# Output:
# Total time taken by take_Time function: 2.00
# Addition: 30
# Total time taken by add function: 0.00