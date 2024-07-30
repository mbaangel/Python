### Variable Scope --->>>

# Simple
def greet():
    print("Hello Developer!")

greet()

# Return Values
def return_greet():
    return "Hello Developer!"

return_greet()
print(return_greet())

# statements
def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hi", "Angel")

# Default argue
def default_arg_greet(name="Angel"):
    print(f"hola, {name}!")

default_arg_greet()

# With a variable number of arguments
def variable_arg_greet(*names):
    for name in names:
        print(f"Hi, {name}!")


variable_arg_greet("Python", "Angel", "MoreDev", "Community")

# With a variable number of keyword arguments
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arg_greet(
    language="Python",
    name="Angel",
    alias="MoreDev",
    age=36
)

# Functions within functions
def outer_function():
    def inner_function():
        print("Function: Hi, Python!")
    inner_function()


outer_function()

# Language features (built-in)
print(len("MoreDev"))
print(type(36))
print("MoreDev".upper())

# Local and global variables / Variables globales y locales
global_var = "Python"


def hello_python():
    local_var = "Hi"
    print(f"{local_var}, {global_var}!")


print(global_var) # print(local_var) Cannot be accessed from outside the function

hello_python()

# Extra
def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count


print(print_numbers("Fizz", "Buzz"))
 