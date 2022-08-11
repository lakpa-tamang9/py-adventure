# Decorators are a very powerful and useful tool in Python
# since it allows programmers to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to extend
# the behaviour of the wrapped function, without permanently modifying it.


def wrapper(func):
    def inner_func():
        print("This is the first section")
        func()
        print("This is the last section")

    return inner_func()


@wrapper
def my_func():
    print("This is the my middle")


my_func()
