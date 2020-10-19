def add_stuff(original_func):
    def function_wrapper():
        value = original_func()
        print(f"The original value was: {value}")
        value = value**2
        print(f"The new value is: {value}")
        return value

    return function_wrapper


@add_stuff
def pie():
    print("First PIE 3.14")
    return 3.14


pi_times_pi = pie()
print(f"LAST pi {pi_times_pi}")