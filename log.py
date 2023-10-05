import time

def timestamp(func):
    def wrapper(*args, **kwargs):
        current_time = time.ctime()
        result = func(*args, **kwargs)
        print(f"Timestamp: {current_time}")
        print(f"Decorated Content: {result}")
        return result
    return wrapper


from log import timestamp


def example_function():
    return "This is an example function."

result = example_function()
