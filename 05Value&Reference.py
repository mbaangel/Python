"""
Value & Reference
"""

# Data types (value)
my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Data types (reference)
my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_int_a)
print(my_list_b)

# Functions with Data by Reference
def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

'''
 * EXERCISE:
 * - Shows examples of "by value" and "by reference" variable assignment, depending on
 * your data type.
 * - Shows examples of functions with variables that are passed "by value" and
 * "by reference", and how they behave in each case when modified.
 * (Understanding these concepts is essential in the vast majority of languages)
 *
 * EXTRA DIFFICULTY (optional):
 * Create two programs that receive two parameters (each) defined as variables previously.
 * - Each program receives, in one case, two parameters by value, and in another case, by reference.
 * These parameters are exchanged between them inside, returned, and their return
 * is assigned to two variables different from the original ones. Next, print the value of the
 * original variables and the new ones, checking that their value has been inverted in the latter.
 * Also check that the original value has been preserved in the first ones.
'''

# Functions with Data by Value

def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# Functions with Data by Reference

def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")

