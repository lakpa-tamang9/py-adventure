# Inheritance: TO inherit object's property from parent class to child class.
# Parent class is the super class that serves as a fundamental class
# child classes are inside the parent class and they share similar property with the parent class.


from turtle import Turtle
from unicodedata import name


class ProgrammingLanguages:
    def __init__(self, name):
        self.name = name

    def application(self):
        print(
            f"{self.name} Programming language are used to build softwares and automation"
        )

    def complexity(self, complex):
        if complex:
            print(f"{self.name} is complex to learn")
        else:
            print(f"{self.name} is easy to learn")

    def popular(self, purpose):
        print(f"{self.name} is popular for {purpose}")


class Python(ProgrammingLanguages):
    def __init__(self, name):
        super().__init__(name)
        # super init inherits the __init__ method from the parent class.


class Javascript(ProgrammingLanguages):
    def __init__(self, name):
        super().__init__(name)

    def popular(self, purpose):
        return super().popular(purpose)


python = Python("Python")
print(python.application())

javascript = Javascript("Javascript")
print(javascript.application())

print(javascript.complexity(complex=True))
print(javascript.popular(purpose="Web development"))
