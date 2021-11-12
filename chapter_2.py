# Adding whitespaces to the string with tabs or newlines

print("\tpython")   #Adding \t infront of the string to print gives us the desired result.
print("\npython")   # adds new line
print("Languages: \nPython\nC++\nJava")
print("Languages: \n\tPython\n\tC++\n\tJava")   #Moving to new line and tab with single line

# rstrip(), lstrip(), and strip() method ensures that no whitespaces exist at the right, left, or both end at once of a string
fav_lanuage = 'python '
print(fav_lanuage.rstrip())
print(fav_lanuage.lstrip())
print(fav_lanuage.strip())

print('ALbert Einstien once said, "A person who never made a mistake never tried anything new."')

#NUMBERS

print(4 + 2.0)

# we can group the long numbers using underscore to make the large number more readable
num = 9000_222_344_3334
print(num)

my_fav_num = 9
print(f"My favourite number is {my_fav_num}")

# import this

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

print(f"Hello {bicycles[0].upper()}, how are you")

bicycles.insert(2, 'hero')  # Adding new element to desired position in the list
print(bicycles)

del bicycles[3] # Deleting the element of the list
print(bicycles)


print(bicycles.pop(2)) # Pop usually removes the last item in the list, however, we can also specify the index of the element we want to pop.

too_expensive = bicycles.remove('trek')
print(f"\n I dont have {too_expensive} as it is very expensive for me")

my_foods = ['a', 'b', 'c']
my_friends_food = my_foods
print(my_foods)
print(my_friends_food)

tup = (3,) #defining a tuple with one element, alwasy use comma.

age_0 = 22
age_1 = 18

print(age_0 >= age_1 and age_1 > 8)

usernames = ['lakpa', 'sonam', 'pujan', 'pawan', 'mahesh', 'admin']
for username in usernames:
    if username == 'admin':
        print(f'Hello {username}.title(), would you like to see a status report?')
    else:
        print(f'Hello {username}.title(), thank you for logging again.')

users = []
for user in users:
    if user == '':
        print('We need to find some users')