def allcaps(func):
    def wrapper():
        result = func()
        print(result.upper())

    return wrapper
def my_test_function():
    return "hello, world!"
