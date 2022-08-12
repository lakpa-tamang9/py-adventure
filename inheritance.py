# Inheritance: TO inherit object's property from parent class to child class.
# Parent class is the super class that serves as a fundamental class
# child classes are inside the parent class and they share similar property with the parent class.

# Polymorphism:  It refers to the use of a single type entity (method, operator or object)
# to represent different types in different scenarios.

# We can use the concept of polymorphism while creating class methods as
# Python allows different classes to have methods with the same name.


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

    def popular(self):
        return "This is popular among data scientists, automation, Machine learning "


class Javascript(ProgrammingLanguages):
    def __init__(self, name):
        super().__init__(name)

    def popular(self):
        return "This is very popular along with HTML and CSS for website development"


# COncept of polymorphism: In the above classes, popular method is inherited from the parent class
# and used in two child classes with different purposes. ALthough they have same name,
# they serve differnt purpose and can be modified accordingly.

python = Python("Python")
# print(python.application())
print(python.popular())
javascript = Javascript("Javascript")
# print(javascript.application())

# print(javascript.complexity(complex=True))
# print(javascript.popular(purpose="Web development"))
