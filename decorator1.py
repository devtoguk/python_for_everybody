def my_decorator(original_func):
    def wrapper():
        print("Do a thing before")

        original_func()

        print("Do a thing after")
    return wrapper


@my_decorator
def greeting():
    print("HELLO WORLD!")


greeting()
