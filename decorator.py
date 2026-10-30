import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper  

@timer
def example_function():
    time.sleep(2)  # Simulating a time-consuming operation
    print("Function execution completed.")

example_function()

@timer
def next_function():
    for i in range(10):
         # Simulating a time-consuming operation
        print(f"Processing item {i + 1}")

next_function()