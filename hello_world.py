# print("Hello world")
# print("Hello World Interpreter!")

# message = "Hello Python world!"
# print(message)

message = "Hello Pythob Crash Course world!"
print(message)

# Any characters inside the single or double quotes are string.
# We can use quotes within the string as well. 

string_1 = 'Hello my name is Lakpa and i am a programmer, "I want to be a good programmer at the end of this course" Thank you'
print(string_1)

# To use 
name = "lakpa tamang"
print(name.title()) #the method title makes the first character of the name to upercase.
# title() is a method. Every methods require parenthesis to be executed.

# print(name.lower(), name.upper())

# Using variables in strings (f-strings)
first_name = "lakpa"
last_name = "dorje"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, my name is {first_name} {last_name}")

# f-strings do not work on python3.5 or earlier. We can use .format() instead.

my_full_name = "{} {}".format(first_name, last_name)





