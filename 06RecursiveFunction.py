"""
Recursive Function
"""

def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)

countdown(100)

"""
* EXERCISE:
* Understand the concept of recursion by creating a recursive function that prints
* numbers from 100 to 0.
*
* EXTRA DIFFICULTY (optional):
* Use the concept of recursion to:
* - Calculate the factorial of a specific number (the function receives that number).
* - Calculate the value of a specific element (according to its position) in the
* Fibonacci sequence (the function receives the position).
"""

def factorial(number: int) -> int:
    if number < 0:
        print("Invalid negative numbers")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number -1)
    
print(factorial(5))


def fibonacci(number: int) -> int:
    if number <= 0:
        print("The position must be greater than zero")
        return 0
    elif number ==1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(5))
