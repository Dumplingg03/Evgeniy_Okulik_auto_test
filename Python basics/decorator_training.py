def decorator(func):
    def wrapper():
        print("начало обертки")
        initial_func = func
        result = initial_func()
        print("конец обертки")
        return result
    return wrapper

def printer():
    print("hello world")

decorator(printer)()

print("\n")

def decorator1(func):
    def wrapper():
        print("начало обертки")
        initial_func = func
        result = initial_func()
        print("конец обертки")
        return result
    return wrapper

@decorator1
def printer1():
    print("hello world")

printer1()