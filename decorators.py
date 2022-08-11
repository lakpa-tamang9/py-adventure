# Decorators are a very powerful and useful tool in Python
# since it allows programmers to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to extend
# the behaviour of the wrapped function, without permanently modifying it.


# def outer_func(func):
#     def inner_func():
#         print("This is the first section")
#         func()
#         print("This is the last section")

#     return inner_func()


# @outer_func
# def my_func():
#     print("Lakpa")

## Example 2

# my_func()
from ast import arg


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


# This means run printer function inside percent and then run inside star
@star
@percent
def printer(msg):
    print(msg)


# printer("lakpa")

## example 3


def outer(func):
    def inner(*args):
        print("High")
        func(*args)
        print("Low")

    return inner


@outer
def show(arg):
    print(arg)


# show("Mid" * 9)

# Advanced example


def details(func):
    def personal_info(*args):
        my_dict = {"Name": "Lakpa", "Age": 26, "Country": ["Nepal", "Korea"]}
        func(*args)
        for countries in my_dict["Country"]:
            print(f"Lakpa lived in {countries}")

    return personal_info


@details
def get_info(arg):
    print(arg)


get_info("Male")
