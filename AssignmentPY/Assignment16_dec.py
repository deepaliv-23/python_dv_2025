import time
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[LOG] Starting '{func.__name__}' with args={args}, kwargs={kwargs} at {time.ctime(start_time)}")
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"[LOG] Finished '{func.__name__}' at {time.ctime(end_time)}. Execution time: {duration:.4f}s")
        return result
    return wrapper

@log_execution
def add(a, b):
    time.sleep(1)
    return a + b

@log_execution
def greet(name):
    time.sleep(0.5)
    return f"Hello, {name}!"

# Example usage:
print(add(5, 3))
print(greet("Deepali"))
