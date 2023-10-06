def my_test_function ()
def allcaps(func):
    def wrapper():
        result = func()
	my_test_function()
        print(result.upper())

    return wrapper
