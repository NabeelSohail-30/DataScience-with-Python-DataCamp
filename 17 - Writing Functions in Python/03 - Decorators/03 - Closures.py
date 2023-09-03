def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))

    return new_func


my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)


def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))

    return new_func


my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)

# Show that there are two variables in the closure
print(len(my_func.__closure__) == 2)


def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))

    return new_func


my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [
    my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])


def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()

    return call_func


new_func = get_new_func(my_special_function)


# Redefine my_special_function() to just print "hello"
def my_special_function():
    print("hello")


new_func()


def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()

    return call_func


new_func = get_new_func(my_special_function)

# Delete my_special_function()
del (my_special_function)

new_func()


def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()

    return call_func


# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

my_special_function()