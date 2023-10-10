def allcaps(func):
    def wrapper(*args, **kwargs):
        result = func()
        print(func(*args, **kwargs).upper())

    return wrapper
