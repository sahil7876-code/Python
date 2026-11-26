def out(func):
    is_running = False

    def wrapper(*args):
        nonlocal is_running
        if is_running:
            return func(*args)
        
        is_running = True
        print("Before")
        result = func(*args)
        print(result)
        print("Print")
        is_running = False

    return wrapper

@out
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

fact(5)