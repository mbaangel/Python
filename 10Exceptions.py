"""
Exceptions
"""

try:
    print(10/0)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"An error has ocurred.")

"""
/*
* EXERCISE:
* Explore the concept of exception handling in your language.
* Force an error in your code, catch the error, print the error,
* and prevent the program from stopping unexpectedly.
* Try dividing "10/0" or accessing a non-existent index
* in a list to try to cause an error.
*
* EXTRA DIFFICULTY (optional):
* Create a function that is capable of processing parameters, but that can also
* throw 3 different types of exceptions (one of them has to
* correspond to a custom exception type created by us, and must be thrown manually) in case of an error.
* - Catch all exceptions from the place where you call the function.
* - Print the type of error.
* - Print if no error has occurred.
* - Print that the execution has finished.
*/
"""

class StrTypeError(Exception):
    pass

def process_params(parameters: list):
    
    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError(
            "The third element cannot be a text string."
        )
    
    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1, 2, 3, 4])
except IndexError as e:
    print("The number of elements in the list must be greater than two.")
except ZeroDivisionError as e:
    print("The second element in the list cannot be a zero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"An unexpected error has ocurred: {e}")
else:
    print("No error has ocurred.")
finally:
    print("The program ends without stopping.")