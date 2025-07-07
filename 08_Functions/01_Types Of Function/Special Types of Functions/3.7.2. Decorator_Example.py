
def   show(func):
    def   mfx(*args, **kwargs):
        arg = ", ".join(str(arg) for arg in args)
        kargs = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with arg: {arg if arg else 0} and kwargs: {kargs if kargs else 0}")
        return func(*args, *kwargs)
    return mfx

@show
def add(a, b, c, name = "Shreyash"):
    print("Addition: ", a+b+c)

@show
def hello():
    print("Hello")

add(10, 20, 30)
hello()
# Output:
# add function takes 3 arguments.
# Addition:  60