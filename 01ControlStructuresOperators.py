### Operators and Control Structures --->>>

# Arithmetic Operators / Operadores aritméticos
suma = 10
suma2 = 15
subtotal = suma + suma2
print(subtotal)
print(f"Addition: 10 + 3 = {10 + 3}")
print(suma)
print(f"Substraction:  10 - 3 = {10 - 3}")
print(f"Multiplication: 10 * 3 = {10 * 3}")
print(f"Division: = 10 / 3 = {10 / 3}")
print(f"Modulus: 10 % 3 = {10 % 3}")
print(f"Exponentiation: { 10 ** 3}")
print(f"Floor division: 10 // 3 = {10 // 3}")

# Comparison Operators / Operadores de comparasión
print(f"Equal: 10 == 3 = {10 == 3}")
print(f"Not equal: 10 != 3 = {10 != 3}")
print(f"Greater than: 10 > 3 = {10 > 3}")
print(f"Less than: 10 < 3 = {10 < 3}")
print(f"Greater than or equal to: 10 >= 3 = {10 >= 3}")
print(f"Less than or equal to: 10 <= 3 = {10 <= 3}")

# Logical Operators / Operadores lógicos
print(f"Returns True if both statements are true: 10 AND 3: {10 + 3 == 13 and 5 - 1 == 4} ")
print(f"Returns True if one of the statements is true: 10 OR 3 {10 + 3 == 13 and 5 - 5 == 4}")
print(f"Reverse the result, returns False if the result is true: 10 + 3 == 14 = {not 10 + 3 == 14}")

#Assigment Operators / Operadores de asignación
my_number = 11
print(my_number)
my_number += 1
print(my_number)
my_number -= 1
print(my_number)
my_number *= 1
print(my_number)
my_number /= 1
print(my_number)
my_number %= 1
print(my_number)
my_number //= 1
print(my_number)
my_number **= 1
print(my_number)

# Identity Operators / Operadores de identidad
my_NewVariable = 1.0 # my_number = 11
print(f"my new variable is = {my_number is my_NewVariable}")
print(f"my new variable is = {my_number is not my_NewVariable}")

# Assignment Operators / Operadores de pertenencia
print(f"'o' in 'more' = {'o' in 'more'}")
print(f"'a' in 'more' = {'a' in 'more'}")

# Bitwaise Operators / Operadores de bits
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 & 3 = {10 | 3}")
print(f"XOR: 10 & 3 = {10 ^ 3}")
print(f"NOT: 10 & 3 = {~10}")
print(f"10 >> 2 = {10 >> 2}")
print(f"10 << 2 = {10 << 2}")

### Control Structures --->>>

# Conditional Statements / Condicionales
my_string = "MoreDev"

if my_string == "MoreDev":
    print("my string is MoreDev")
elif my_string == "Brais":
    print("my string is MoreDev or Brais")
else:
    print("My string is NOT MoreDev")

# Iterables / Iterativas
for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Try... Except
try:
    print(10 / 1)
except:
    print("An error has occurred")
finally:
    print("Exception handling has been executed correctly.")

# EXTRA
"""* Create a program that prints all the numbers included through the console
 * between 10 and 55 (inclusive), even, and that are neither 16 nor multiples of 3."""
for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)


