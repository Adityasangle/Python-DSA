#---------------------------------------------
# def format(func):
#     def inner(name):
#         print("---------------")
#         func(name)
#         print("---------------")
#     return inner

# def print_name(name):
#     print(f"Hey {name}, WELCOME!")


# obj = format(print_name)
# obj("Aditya")
#-----------------------------------------------
#Insread of calling the function obj two times, we can decorate print name with format
def format(func):
    def inner(name):
        print("---------------")
        func(name)
        print("---------------")
    return inner

@format
def print_name(name):
    print(f"Hey {name}, WELCOME!")


print_name("Aditya")
#=-------------------------------------------------
#Example 3
import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)