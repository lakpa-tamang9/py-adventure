# Inheritance: TO inherit object's property from parent class to child class.
# Parent class is the super class that serves as a fundamental class
# child classes are inside the parent class and they share similar property with the parent class.


from unicodedata import name


class ProgrammingLanguages:
    def __init__(self, name):
        self.name = name

    def application(self):
        print(
            f"{self.name} Programming language are used to build softwares and automation"
        )


class Python(ProgrammingLanguages):
    def __init__(self, name):
        super().__init__(name)
        # super init inherits the __init__ method from the parent class.


class Javascript(ProgrammingLanguages):
    def __init__(self, name):
        super().__init__(name)


python = Python("Python")
print(python.application())

javascript = Javascript("Javascript")
print(javascript.application())
